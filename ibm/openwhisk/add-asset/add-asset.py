

import sys

def main(params):
    try:
        orig = params['__ow_body']
        decoded = params['__ow_body'].decode('base64').strip()
        return {"body": decoded}
    except:
        return {"body": "Could not decode body from Base64."}