import json
import requests

ROOT_ENDPOINT = "https://ntrs.nasa.gov/api"
def get_down_endpoint(_id: str, _filename: str):
    return ROOT_ENDPOINT + '/' + _id + '/' + _filename

with open('out.txt', 'r') as f:
    response = json.load(f)

for i in range(3):
    id = response['results'][i]['id']
    print(id)