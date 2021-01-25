#####
import json
import pprint
import requests
import pandas as pd 
import operator
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

#### Using request to load and read the API
#https://www.digitalocean.com/community/tutorials/getting-started-with-python-requests-get-requests


URL = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization": "318fcd11-c5f1-4180-8420-4994c3a5705e"}
r = requests.get(url= URL, headers=headers)
#print(r.status_code)
raw_data = json.loads(r.text)
#pprint.pprint(raw_data)

# Endpoints
link = raw_data['links']


my_enpoints_list = []

for loop_endpoint in link:
    if type(loop_endpoint) == dict:
        if "href" in loop_endpoint.keys():
            local_endpoint = loop_endpoint["href"]
            my_enpoints_list.append(local_endpoint)

#print(my_enpoints_list)
#print(len(my_enpoints_list))

# id
areas = raw_data["stop_areas"]
#print('type of areas', type(areas))

my_id = []
for loop_area in areas:
    if type(loop_area) == dict:
        if "id" in loop_area.keys():
            local_id = loop_area["id"]
            my_id.append(local_id)
        #else:
            #print("Missing key id")
    #else:
        #print(f"Unexpected format {type(loop_area)}")
#print(my_id_list)



# name
my_gare = []

for loop_gare in areas:
    if type(loop_gare) == dict:
        if "label" in loop_gare.keys():
            local_gare = loop_gare["label"]
            my_gare.append(local_gare)
        #else:
            #print("Missing key label")
   #else:
        #print(f"Unexpected format {type(loop_gare)}")

#print(my_gare)


my_coord = []

for loop_coord in areas:
    if type(loop_coord) == dict:
        if "coord" in loop_coord.keys():
            local_coord = loop_coord["coord"]
            my_coord.append(local_coord)
        #else:
            #print("Missing key coord")
    #else:
        #print(f"Unexpected format {type(loop_coord)}")

#print(my_coord)





############ Creating CSV
# CSV info station
data = {'id':my_id, 'name':my_gare, 'coord':my_coord}

info = pd.DataFrame(data)
#print(info)

with open('my_gare.csv', 'w') as f:
    info.to_csv(f, encoding='utf-8') 


# CSV endpoints
links = {'endpooints': my_enpoints_list }
endpoint = pd.DataFrame(links)
##print(endpoint)

with open('my_links.csv', 'w') as f:
    endpoint.to_csv(f, encoding='utf-8') 

################




# Request arrival and departure

# arrival
arrivals = "https://api.sncf.com/v1/coverage/sncf/stop_areas/stop_area:OCE:SA:87722025/arrivals"
headers = {"Authorization": "318fcd11-c5f1-4180-8420-4994c3a5705e"}

response_arrivals = requests.get(url= arrivals, headers= headers)
#print(response_arrivals.status_code)
data_arrival = json.loads(response_arrivals.text)

# departure
departures = "https://api.sncf.com/v1/coverage/sncf/stop_areas/stop_area:OCE:SA:87686006/departures"
response_departures = requests.get(url=departures, headers= headers)
#print(response_departures.status_code)
data_departure = json.loads(response_departures.text)
