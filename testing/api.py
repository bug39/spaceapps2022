import json
import requests

ROOT_ENDPOINT = "https://ntrs.nasa.gov/api"
get_endpoint = lambda path: ROOT_ENDPOINT + '/' + path
search_point = get_endpoint("citations/search")
query = {
    'abstract': 'pluto'
}
response = requests.post(search_point, params=query)
with open('out.txt', 'w') as f:
    json.dump(json.loads(response.content), f, indent=4, separators=(", ", ": "))