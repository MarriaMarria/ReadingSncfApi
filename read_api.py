#####
import json
import logging
import pprint
import requests
import pandas as pd 
import operator
######

##### Reading the file with opn
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


class ReadingSncfApi():

    logging.basicConfig(filename = "info_sncf.log", 
    level= logging.INFO, 
    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')

    logging.info('Request api -- start')
        
    def __init__(self):
        self.URL = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
        self.headers = {"Authorization": "318fcd11-c5f1-4180-8420-4994c3a5705e"}
        self.raw_data = None
        self.my_endpoints_list = []
        self.my_id_list = []
        self.my_list_station = []
        self.my_list_coord = []
        logging.info('Request api -- start')
    

    
    def request_JSON(self):

        
        try:
            r = requests.get(url= self.URL, headers=self.headers)
          
            #print(r.status_code)
            self.raw_data = json.loads(r.text)
            #print(type(raw_data))
            #pprint.pprint(raw_data)
            with open("marwa_sncf.json", mode="w+", encoding='utf-8') as f:
                json.dump(r.json(), f, sort_keys=True, indent=4)
        except:
            logging.info('Error: file not found, cannot access the file')
        
        logging.info('Request api -- end')

        return self.raw_data

    def save_my_json(self):
        self.my_log.info('saving json from api -- start')

        try:
            with open("marwa_sncf.json") as file:   
                self.data = json.load(file)
        except OSError:
            logging.info("Error: file isn't saved")

        logging.info('saving json from api -- end')

    def my_endpoints(self):

        self.link = self.raw_data['links']

        for k, loop_endpoint in enumerate(self.link):
            if type(loop_endpoint) == dict:
                if "href" in loop_endpoint.keys():
                    local_endpoint = loop_endpoint["href"]
                    self.my_endpoints_list.append(local_endpoint)
                else:
                    self.my_log.info("Currently in endpoints, the key 'href' is missing in %s" %k)
            else:
                self.my_log.info("Currently in endpoints, format is not a dict, check condition")
        
        

    def my_id(self):
        
        self.areas = self.raw_data["stop_areas"]

        for k, loop_id in enumerate(self.areas):
            if type(loop_id) == dict:
                if "id" in loop_id.keys():
                    local_id = loop_id["id"]
                    self.my_id_list.append(local_id)
                else:
                    logging.info("Currently in id, the key 'href' is missing in %s" %k)
            else:
                logging.info("Currently in id, format is not a dict, check condition")
        

    def my_station_name(self):
        self.areas = self.raw_data["stop_areas"]

        for k, loop_gare in enumerate(self.areas):
            if type(loop_gare) == dict:
                if "label" in loop_gare.keys():
                    local_gare = loop_gare["label"]
                    self.my_list_station.append(local_gare)
                else:
                    logging.info("Currently in station name, the key 'href' is missing in %s" %k)
            else:
                logging.info("Currently in station name, format is not a dict, check condition")
        

    def my_coord(self):

        areas = self.raw_data["stop_areas"]

        for k, loop_coord in enumerate(areas):
            if type(loop_coord) == dict:
                if "coord" in loop_coord.keys():
                    local_coord = loop_coord["coord"]
                    self.my_list_coord.append(local_coord)
                else:
                    logging.info("Currently in coord, the key 'href' is missing in %s" %k)
            else:
                logging.info("Currently in coord format is not a dict, check condition")


   
    def csv_station(self):

        self.data = {'id':self.my_id_list, 'name':self.my_list_station, 'coord':self.my_list_coord}

        info = pd.DataFrame(self.data)
        #print(info)

        with open('my_gare.csv', 'w') as f:
            self.station_csv = info.to_csv(f, encoding='utf-8') 

        

    def create_csv_endpoints(self):
        # CSV endpoints
        links = {'endpoints': self.my_endpoints_list}
        endpoint = pd.DataFrame(links)
        ##print(endpoint)

        with open('my_links.csv', 'w') as f:
            endpoint.to_csv(f, encoding='utf-8') 

        ################



if __name__ == '__main__':
    logging.basicConfig(filename = "info_sncf.log", 
    level= logging.INFO, 
    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')
    logging.info('Request api -- start')


    my_class = ReadingSncfApi()
    my_class.request_JSON()
    my_class.my_endpoints()
    my_class.my_id()
    my_class.my_station_name()
    my_class.my_coord()
   #print(my_class.my_list_coord) #print pour afficher valeur
    my_class.csv_station()
    my_class.create_csv_endpoints()