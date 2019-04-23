# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import sys
from json import load
from os import getenv

import wiotp.sdk.device
import _thread
import logging
import nest


from flask import Flask, jsonify
from time import sleep

app = Flask(__name__)

authURL = ""
pin = ""
napi = None

pause = False
### Getting Data from NestAPI (hitting the webui requires selenium which is a pain in the ass and not instructive)
with open("config.json" , 'r') as f:
    config = load(f)


## Endpoints ###########################################################################################################
@app.route('/')
def root():
    return jsonify({"message" : "baz to your athsmar"})

@app.route('/get-auth-url')
def getAuthURL():
    global authURL
    return jsonify({"url" : authURL})

@app.route('/set-pin/<set_pin>')
def setPIN(set_pin):
    global pin
    pin = set_pin
    return jsonify({"pin" : pin})

@app.route("/pause")
def pause():
    global pause
    pause = True
    return jsonify({"message" : "shim has been paused"})

@app.route("/play")
def play():
    global pause
    pause = False
    return jsonify({"message" : "shim is in motion"})

## Backend #############################################################################################################


def relay_data():

    client_id = config['nest']['client_id']
    client_secret = config['nest']['client_secret']
    access_token_cache_file = 'nest.json'
    global napi
    napi = nest.Nest(client_id=client_id, client_secret=client_secret, access_token_cache_file=access_token_cache_file)
    logging.info("established nest connection")
    logging.info("napi.authorization_required: %s", str(napi.authorization_required))
    if napi.authorization_required:
        global authURL
        authURL = napi.authorize_url
        logging.info('auth url set, pls visit /get-auth-url then /set-pin/<pin>')
        global pin
        while pin=="":
            sleep(0.5)
        logging.info('recieved pin: %s' % pin)
        napi.request_token(pin)
        logging.info("i think it worked!")
        pin =""
    else:
        logging.info("no auth required.")

    #     from requests import get
    #     r = get(napi.authorize_url)
    #
    # pin = "WECQPAZN"
    #

    ## Connect to WatsonIoT ############################################################################################
    deviceOptions = []
    deviceCli = []
    for i in range(0, len(napi.structures[0].thermostats)):
        dev_id = napi.structures[0].thermostats[i].device_id
        deviceOptions.append({
            "identity": {"orgId": config[dev_id]['org_id'],
                         "typeId": config[dev_id]['dev_type'],
                         "deviceId": config[dev_id]['device_id']
                         },
            "auth": {"token": config[dev_id]['token']},
        })
        deviceCli.append(wiotp.sdk.device.DeviceClient(deviceOptions[i]))
        deviceCli[i].connect()


    def myOnPublishCallback():
        logging.info("Confirmed event %s received by IoTF\n" % str(payload))
    while True:
        global pause
        if pause:
            logging.info("paused. please go to <base_url>/play to continue")
            sleep(10)
            continue
        for i in range(0, len(napi.structures[0].thermostats)):
            t = napi.structures[0].thermostats[i]
            payload = {
                "humidty" : t.humidity,
                "hvac_state" : t.hvac_state,
                "temperature" : t.temperature
            }
            # camera snapshots ? napi.structures[0].cameras[0].snapshot_url
            success = deviceCli[i].publishEvent("tempreading", "json", payload, qos=1, on_publish=myOnPublishCallback)
            if success:
                logging.info("status of update is good")
            else:
                logging.warning("staus is not so good.")
            sleep(15)
        sleep(15)



def flaskThread():
    app.run(host='0.0.0.0', port=int(port), use_reloader=False)

port = getenv('PORT', '5000')

########################################################################################################################
## Main: start Flask, turn on the scheduler; run forever.

if __name__ == "__main__":
    logging.basicConfig(level= logging.INFO)
    _thread.start_new_thread(flaskThread,())
    relay_data()

