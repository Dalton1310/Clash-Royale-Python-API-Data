import urllib.request
import json

with open("mykey.txt") as f:
    my_key = f.read().strip()

base_url = "https://api.clashroyale.com/v1"
endpoint = "/cards"


# Prepare the request with the Authorization header (fixing the dictionary issue)
headers = {
    "Authorization": f"Bearer {my_key}"
}

# Construct the request with the proper headers
request = urllib.request.Request(
    base_url + endpoint, headers=headers
)

# Send the request and get the response
response = urllib.request.urlopen(request).read().decode("utf-8")
#print(response)

data = json.loads(response)

# Write the data to a JSON file using UTF-8 encoding
with open("ClashRoyaleView.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)