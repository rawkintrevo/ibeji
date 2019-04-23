import nest

client_id = ""
client_secret = ""
access_token_cache_file = 'nest.json'
napi = nest.Nest(client_id=client_id, client_secret=client_secret, access_token_cache_file=access_token_cache_file)
if napi.authorization_required:
    # todo finish the Nest setup script. spit out json