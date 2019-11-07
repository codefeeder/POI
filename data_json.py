import requests
import json
overpass_url = "http://overpass-api.de/api/interpreter"

# overpass_query = """
# [out:json];
# area["ISO3166-1"="DE"][admin_level=2];
# (node["amenity"="biergarten"](area);
#  way["amenity"="biergarten"](area);
#  rel["amenity"="biergarten"](area);
# );
# out center;
# """

overpass_query = """
[out:json];
area["ISO3166-2"="IN-DL"];
node["amenity"=](area);
out;
"""


# response = requests.get(overpass_url,params={'data': overpass_query})
# data = response.json()

# print(data)
with open('data.json', 'r') as f:
    data = json.load(f)