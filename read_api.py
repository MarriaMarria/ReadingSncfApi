
#####
import json
import pprint
import requests

######


"""json_data = None
with open("stop_areas.json", 'r') as f:
    data_api = f.read()
    sncf_data_json = json.loads(data_api)
pprint.pprint(sncf_data_json)
"""


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


  
# api-endpoint 


# sending get request and saving the response as response object
URL = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization": "0157b284-3cc3-4799-a1ab-79dc2761d274"}
request_url = requests.get(url= URL, headers=headers)
print(request_url)
print(request_url.json())
"""sncf_data_json = json.loads(request_url)

# extracting data in json format 
sncf_data_json.json()
  
 """