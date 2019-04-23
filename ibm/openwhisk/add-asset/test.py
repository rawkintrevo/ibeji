from requests import get, post


base_url="https://us-south.functions.cloud.ibm.com/api/v1/web/digitwin_digitwin/ibeji/add-asset-image"
r = post(base_url, data= open("/home/rawkintrevo/gits/ibeji/ibm/examples/data/rawkintrevos-2flat.jpg", 'rb'))