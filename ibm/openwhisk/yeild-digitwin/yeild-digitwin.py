import sys

def main(params):
    render_id = params.get('id', False)
    if not render_id:
        return {"error": "idk who or what you're playing at."}

    # 3. locations to render sensor output (relative to image (should reference image))
    # get(render_id)
    render_data = {
        "image_loc" : "...",
        "sensors"   : { # and how big?
            "tmeter" : { 'x' : 400, 'y' : 500 },
            "hmeter" : { 'x' : 400, 'y' : 480 },
            "hvacstatus" : {'x' : 400, 'y' : 520 }
        }
    }
    # 1. Picture of the asset ( could be svg- could be blueprint, photo, etc etc.)
    # get(render_data['image_loc']


# 2. Methods to render sensor output

# 1. where to find states of each sensor
# 1. a call to get the state of the sensors