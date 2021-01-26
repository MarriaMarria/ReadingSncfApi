#####
import json
import logging
import pprint
import requests
import pandas as pd 
import operator
######

##### Reading the file with open
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


logging.basicConfig(filename = "info_sncf.log", level= logging.INFO, format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')

URL = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization": "318fcd11-c5f1-4180-8420-4994c3a5705e"}
def main():

    def request_JSON():
        try:
            r = requests.get(url= URL, headers=headers)
            
            print(r.status_code)
            raw_data = json.loads(r.text)
            #print(type(raw_data))
            #pprint.pprint(raw_data)
            with open("marwa_sncf.json", mode="w+", encoding='utf-8') as f:
                json.dump(r.json(), f, sort_keys=True, indent=4)
        except:
            logging.info('Error: file not found, cannot access the file')
        
        return raw_data
    def_request_json = request_JSON()
    #pprint.pprint(def_request_json)

    def save_my_json():
        with open("marwa_sncf.json") as file:   
            data = json.load(file)

    save_my_json()


    def my_endpoints():
        #my_json = save_my_json()
        link = def_request_json['links']
        #pprint.pprint(link)
        my_endpoints_list = []

        for k, loop_endpoint in enumerate(link):
            if type(loop_endpoint) == dict:
                if "href" in loop_endpoint.keys():
                    local_endpoint = loop_endpoint["href"]
                    my_endpoints_list.append(local_endpoint)
                else:
                    logging.info("Currently in endpoints, the key 'href' is missing in %s" %k)
            else:
                logging.info("Currently in endpoints, format is not a dict, check condition")
        
        return my_endpoints_list

    def_endpoints = my_endpoints()
    print(def_endpoints)


    def my_id():
        # id
        areas = def_request_json["stop_areas"]
        #print('type of areas', type(areas))

        my_id = []
        for k, loop_id in enumerate(areas):
            if type(loop_id) == dict:
                if "id" in loop_id.keys():
                    local_id = loop_id["id"]
                    my_id.append(local_id)
                else:
                    logging.info("Currently in id, the key 'href' is missing in %s" %k)
            else:
                logging.info("Currently in id, format is not a dict, check condition")
        
        return my_id

    def_id = my_id()
    #print(def_id)

    def my_station_name():
        areas = def_request_json["stop_areas"]
        my_gare = []

        for k, loop_gare in enumerate(areas):
            if type(loop_gare) == dict:
                if "label" in loop_gare.keys():
                    local_gare = loop_gare["label"]
                    my_gare.append(local_gare)
                else:
                    logging.info("Currently in station name, the key 'href' is missing in %s" %k)
            else:
                logging.info("Currently in station name, format is not a dict, check condition")
        
        return my_gare

    def_station_name = my_station_name()
    #print(def_station_name)

    def my_coord():

        areas = def_request_json["stop_areas"]
        my_coord = []

        for k, loop_coord in enumerate(areas):
            if type(loop_coord) == dict:
                if "coord" in loop_coord.keys():
                    local_coord = loop_coord["coord"]
                    my_coord.append(local_coord)
                else:
                    logging.info("Currently in coord, the key 'href' is missing in %s" %k)
            else:
                logging.info("Currently in coord, format is not a dict, check condition")
        
        return my_coord

    def_coord= my_coord()
    #print(def_coord)


    def csv_station():

        ############ Creating CSV
        # CSV info station
        data = {'id':def_id, 'name':def_station_name, 'coord':def_coord}

        info = pd.DataFrame(data)
        #print(info)

        with open('my_gare.csv', 'w') as f:
            station_csv = info.to_csv(f, encoding='utf-8') 
        
        
    csv_station()

    def create_csv_endpoints():
        # CSV endpoints
        links = {'endpooints': def_endpoints }
        endpoint = pd.DataFrame(links)
        ##print(endpoint)

        with open('my_links.csv', 'w') as f:
            endpoint.to_csv(f, encoding='utf-8') 

        ################



main()