#####
import json
import pprint
import requests
import pandas as pd
######

##### Reading the file with opan
'''
json_data = None
with open("stop_areas.json", 'r') as f:
    data_api = f.read()
    sncf_data_json = json.loads(data_api)
pprint.pprint(sncf_data_json)
'''

#### Adding a station with load and update (not the right format JSON)
"""
new_area = {'Station': 'Republique', 'Departement': '75'}

with open('stop_areas.json') as f:
    add_station = json.load(f)

    add_station.update(new_area)

with open('stop_areas.json', 'a') as f:
    json.dump(add_station, f)
    
"""


###### What's an Endpoint ?
"""

It's one end of a communication channel, 
so often this would be represented as the URL of a server or service.



An endpoint is the 'connection point' of a service, tool, or application accessed over a network. 
In the world of software, any software application that is running and "listening" for connections uses an endpoint as the "front door."
When you want to connect to the application/service/tool to 
exchange data you connect to its endpoint


https://stackoverflow.com/questions/2122604/what-is-an-endpoint
"""



#### Using request to load and read the API

URL = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization": "0157b284-3cc3-4799-a1ab-79dc2761d274"}
r = requests.get(url= URL, headers=headers)
raw_data = json.loads(r.text)



areas = raw_data["stop_areas"]
print(type(areas))

area = areas[0]
my_id_list = []

for loop_area in areas:
    if type(loop_area) == dict:
        if "id" in loop_area.keys():
            local_id = loop_area["id"]
            my_id_list.append(local_id)

print(my_id_list)



#print("Unexpected format (dict expected):",
# type(loop_Area))

#print(type(area), area)

#print(area.keys())

#https://www.digitalocean.com/community/tutorials/getting-started-with-python-requests-get-requests


'''
### Passing from JSON to CSV the enpoints
json_data = None
json_file = 'stop_areas.json'  
with open(json_file) as json_data:     
  data = json.load(json_data)
pprint.pprint(data)

print(data.keys())


with open('data', encoding='utf-8-sig') as f:
    sncf_api_file = pd.read_json(f)
my_csv = sncf_api_file.to_csv('data.csv', encoding='utf-8', index=False)
sncf_csv = pd.read_csv("data.csv")
'''