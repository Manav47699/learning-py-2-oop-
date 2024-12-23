#how to connect to an API using Python

import requests

base_url = "https://developer.spotify.com/documentation/web-api"

def get_info(name):
    url = f"{base_url}/artist/{name}"
    response = requests.get(url)
    print (response)

artist_name = "Emiway"
get_info (artist_name)


