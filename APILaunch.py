import urllib.request
import json

# Read API key from file
with open("mykey.txt") as f:
    my_key = f.read().strip()

base_url = "https://api.clashroyale.com/v1"
headers = {
    "Authorization": f"Bearer {my_key}"
}

def fetch_endpoint_data(endpoint):
    """
    Fetch data from the Clash Royale API based on the provided endpoint.
    """
    url = base_url + endpoint
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request).read().decode("utf-8")
    return json.loads(response)

# Variable to hold the data for the selected endpoint
endpoint_data = {}
