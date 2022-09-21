import json
import requests

ROOT_ENDPOINT = "https://ntrs.nasa.gov/api"
get_endpoint = lambda path: ROOT_ENDPOINT + '/' + path
search_point = get_endpoint("citations/search")
query = {
    'center': "JPL"
}
#response = requests.post(search_point, params=query)
