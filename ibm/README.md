

# IBM

We could also use IBM's Watson IoT Platform instead of Flink.



## Notes on Watson IoT- don't commit. 

Asset needs to have interfaces and create them. (State is only read if interface exists).


## Steps

1. Get Device IDs for your nest thermostat(s)
1. Run `setup-nest.py`, copy nest.json to `cf-app-shim`
1. rename `cf-app-shim/config.json.template` to `cf-app-shim/config.json`  
1. Create Devices in WatsonIoT Platform
1. Update `config.json` with the auth tokens you get (and org-id)