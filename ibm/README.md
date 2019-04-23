

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


## `data`

`Floor_Plan.svg` is a bootleg blueprint I made of the floors in my 2 flat (both are the same).

## What do we need to Render and Image:

1. Picture of the asset ( could be svg- could be blueprint, photo, etc etc.)
2. Methods to render sensor output
3. locations to render sensor output (relative to image (should reference image))
1. where to find states of each sensor
1. a call to get the state of the sensors
