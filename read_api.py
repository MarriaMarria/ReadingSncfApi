#####
import json
import logging
import pprint
import requests
import pandas as pd 
import datetime

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


        
    def __init__(self):
        self.URL = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
        self.headers = {"Authorization": "318fcd11-c5f1-4180-8420-4994c3a5705e"}
        self.raw_data = None
        self.name = None
        self.my_endpoints_list = []
        self.my_id_list = []
        self.my_list_station = []
        self.my_list_coord = []
        self.url_paris_lyon = "https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025"
        self.transfers_list = []
        self.stop_list = []
        self.stop_time = 0
 

    def request_JSON(self):
        logging.info('Request api -- start')
        try:
            r = requests.get(url= self.URL, headers=self.headers)
          
            #print(r.status_code)
            self.raw_data = json.loads(r.text)
            #self.file_name = self.name + '.json'
            #print(type(self.raw_data))
            #pprint.pprint(self.raw_data)
            with open("marwa_sncf.json", mode="w+") as f:
                json.dump(r.json(), f, sort_keys=True, indent=4)
        except OSError:
            logging.info('Error: file not found, cannot access the file')
        
        
        logging.info('Request api -- end')


    def save_my_json(self):
        logging.info('saving json from api -- start')

        try:
            with open("marwa_sncf.json") as file:   
                self.data = json.load(file)
        except OSError:
            logging.info("Error: file isn't saved")

        logging.info('saving json from api -- end')


    def my_endpoints(self):

        links = self.raw_data['links']
        logging.info('append endpoint to list : start')

        for k, loop_endpoint in enumerate(links):
            if type(loop_endpoint) == dict:
                if "href" in loop_endpoint.keys():
                    local_endpoint = loop_endpoint["href"]
                    self.my_endpoints_list.append(local_endpoint)
                else:
                    logging.info("Currently in endpoints, the key 'href' is missing in %s" %k)
            else:
                logging.info("Currently in endpoints, format is not a dict, check condition")

        logging.info('append endpoint to list : end')


    def my_id(self):
        logging.info('append id to list : start')
        areas = self.raw_data["stop_areas"]

        for k, loop_id in enumerate(areas):
            if type(loop_id) == dict:
                if "id" in loop_id.keys():
                    local_id = loop_id["id"]
                    self.my_id_list.append(local_id)
                else:
                    logging.info("Currently in id, the key 'href' is missing in %s" %k)
            else:
                logging.info("Currently in id, format is not a dict, check condition")
        logging.info('append id to list : end')


    def my_station_name(self):
        areas = self.raw_data["stop_areas"]
        
        logging.info('append station to list : start')

        for k, loop_gare in enumerate(areas):
            if type(loop_gare) == dict:
                if "label" in loop_gare.keys():
                    local_gare = loop_gare["label"]
                    self.my_list_station.append(local_gare)
                else:
                    logging.info("Currently in station name, the key 'href' is missing in %s" %k)
            else:
                logging.info("Currently in station name, format is not a dict, check condition")
        
        logging.info('append station to list : end')


    def my_coord(self):

        areas = self.raw_data["stop_areas"]
        
        logging.info('append coord to list : start')

        for k, loop_coord in enumerate(areas):
            if type(loop_coord) == dict:
                if "coord" in loop_coord.keys():
                    local_coord = loop_coord["coord"]
                    self.my_list_coord.append(local_coord)
                else:
                    logging.info("Currently in coord, the key 'href' is missing in %s" %k)
            else:
                logging.info("Currently in coord format is not a dict, check condition")
        
        logging.info('append coord to list : start')


    def csv_station(self):
        
        logging.info('create station csv : start')

        try:
            self.data = {'id':self.my_id_list, 'name':self.my_list_station, 'coord':self.my_list_coord}

            info = pd.DataFrame(self.data)
            #print(info)

            info.to_csv('my_gare.csv', encoding='utf-8')
        except TypeError:
            logging.info('failed to create csv')

        
        logging.info('create station csv : end')


    def csv_endpoints(self):

        logging.info('create endpoints csv : start')

        try:
            # CSV endpoints
            self.links = {'endpoints': self.my_endpoints_list}
            endpoint = pd.DataFrame(self.links)
            ##print(endpoint)

            endpoint.to_csv('my_links.csv', encoding='utf-8') 
        except TypeError:
            logging.info('Failed to create endpoint csv')

        logging.info('create station csv : end')


    def request_api_paris_lyon(self):
        logging.info("request paris - lyon : start")

        try:
            journey_json = requests.get(url=self.url_paris_lyon, headers= self.headers)
            #print(journay_json.status_code)
            self.data_journey = json.loads(journey_json.text)
            #self.file_name = self.name + '.json'
            with open('m_sncf.json', mode="w+") as f:
                json.dump(journey_json.json(), f, sort_keys=True, indent=4)
        except OSError:
            logging.info('Error: file not found, cannot access the file')
         

        logging.info("request paris - lyon : start")


    def save_my_paris_lyon_json(self):
        logging.info('saving json from api -- start')

        try:
            with open("m_sncf.json") as file:   
                data = json.load(file)
        except IOError:
            logging.info("Error: file isn't saved")

        logging.info('saving json from api -- end')

    def nbr_of_train_change(self):

        self.journeys = self.data_journey["journeys"]

        logging.info("append transfers to list : strat")

        for k, loop_transfers in enumerate(self.journeys):
            if type(loop_transfers) == dict:
                if "nb_transfers" in loop_transfers.keys():
                    local_transfers = loop_transfers['nb_transfers']
                    self.transfers_list.append(local_transfers)
                else:
                    logging.info("Currently in train changs, the key 'nb_transfers' is missing in %s" %k)
            else:
                logging.info("Currently in train changes format is not a dict, check condition")

        logging.info("append transfers to list : end")


    def collectiong_station_name(self):

        self.journeys = self.data_journey["journeys"]
        self.journey = self.journeys[0]
        
        for names in self.journeys:
            if "name" in names.keys():
                print(names)
        
        #### tree of key from to find where are the labels
        #from_name = self.journey["sections"][0]['from']
        #pprint.pprint(from_name.keys())
        
        sections = self.journey['sections']
        #print(type(sections)) #list

        steps = (sections[1]['stop_date_times']) #liste
        self.nbr_stations = len(steps) - 2 #doesn't take departure and arrival station

        ######### Finding the names of the differentes stations
        for i, stop in enumerate(steps):
            #print(type(stop))
            #print(stop["stop_point"]['label'], i)
            if i != 0:
                self.stop_list.append(stop['stop_point']['label'])
                
            if "arrival_date_time" in stop.keys():
                arrival = stop["arrival_date_time"]
                self.format_arrival_time = datetime.datetime.strptime(arrival,"%Y%m%dT%H%M%S")


            if "departure_date_time" in stop.keys():
                departure = stop["departure_date_time"]
                self.format_departure_time = datetime.datetime.strptime(departure,"%Y%m%dT%H%M%S")
        
            self.stop_time = self.format_departure_time - self.format_arrival_time
