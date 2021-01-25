#####
import json
import pprint
import requests
import pandas as pd 
import operator
######

headers = {"Authorization": "318fcd11-c5f1-4180-8420-4994c3a5705e"}

# journey
journey = "https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025"
journey_json = requests.get(url=journey, headers= headers)
#print(journay_json.status_code)
data_journey = json.loads(journey_json.text)
#pprint.pprint(data_journey)


journeys = data_journey["journeys"]
journey = journeys[0]

#print(type(journey)) #dict
########

'''from_departure = sections['from']
print(type(from_departure['embedded_type']))

for key in from_departure.keys():
    print(type(from_departure[key]), key)'''

## definition of the type of all keys in section
'''
for key in journey.keys():
    print(type(journey[key]), key)

<class 'str'> status
<class 'dict'> distances : 
<class 'list'> links
<class 'list'> tags
<class 'int'> nb_transfers
<class 'dict'> durations : 
<class 'str'> arrival_date_time
<class 'list'> calendars
<class 'str'> departure_date_time
<class 'str'> requested_date_time
<class 'dict'> fare
<class 'dict'> co2_emission
<class 'str'> type
<class 'int'> duration
<class 'list'> sections : liste avec des dictionnaires 

                (<type 'dict'>, u'from')
                (u'codes', <type 'list'>)
                (u'name', <type 'unicode'>)
                (u'links', <type 'list'>)
                (u'coord', <type 'dict'>)
                (u'label', <type 'unicode'>)
                (u'administrative_regions', <type 'list'>)
                (u'timezone', <type 'unicode'>)
                (u'id', <type 'unicode'>)
                (<type 'unicode'>, u'embedded_type')
                (<type 'unicode'>, u'id')
                (<type 'int'>, u'quality')
                (<type 'dict'>, u'stop_area')

                        (u'name', <type 'unicode'>)
                        (u'links', <type 'list'>)
                        (u'coord', <type 'dict'>)
                        (u'label', <type 'unicode'>)
                        (u'administrative_regions', <type 'list'>)
                        (u'timezone', <type 'unicode'>)
                        (u'id', <type 'unicode'>)


                (<type 'unicode'>, u'name') 

        (<type 'list'>, u'links')
        (<type 'unicode'>, u'arrival_date_time')
        (<type 'unicode'>, u'departure_date_time')
        (<type 'dict'>, u'to')

            (<type 'unicode'>, u'embedded_type')
            (<type 'dict'>, u'stop_point')
            (<type 'int'>, u'quality')
            (<type 'unicode'>, u'name')
            (<type 'unicode'>, u'id')

        (<type 'dict'>, u'co2_emission')
        (<type 'int'>, u'duration')
        (<type 'unicode'>, u'type')
        (<type 'unicode'>, u'id')
        (<type 'unicode'>, u'mode')
''' 
#print(journey.keys())


#### Extracting the number of tranfert in the first section
#sections = station['sections']
#print(transfers)

transfers_list = []
for k, loop_transfers in enumerate(journeys):
    if type(loop_transfers) == dict:
        if "nb_transfers" in loop_transfers.keys():
            local_transfers = loop_transfers['nb_transfers']
            transfers_list.append(local_transfers)

print(transfers_list) #=0

names_station = []

for names in journeys:
    if "name" in names.keys():
        print(names)
#### save data in json file

#### tree of key from to find where are the labels
from_name = journey["sections"][0]['from']
#pprint.pprint(from_name.keys())

sections = journey['sections']
#print(type(sections)) #list
steps = (sections[1]['stop_date_times']) #liste
nbr_stations = len(steps) - 2 #doesn't take departure and arrival station


######### Finding the names of the differentes stations
stop_list = []
for i, stop in enumerate(steps):
    #print(type(stop))
    #print(stop["stop_point"]['label'], i)
    if i != 0:
        stop_list.append(stop['stop_point']['label'])

print('name of station : ', stop_list)


######### Duration time between station


arrival_time = []
for k, loop_arrival_time in enumerate(journeys): 
    #print(type(loop_arrival_time), k) = dict
        for loop_section in loop_arrival_time['sections']: #date_time of each section = gare
            #print("arrival ==> ",loop_section["arrival_date_time"], k)            
            arrival_time.append(loop_section["arrival_date_time"])
print("arrival", arrival_time)

departure_time = []
for j, loop_departure_time in enumerate(journeys): 
    #print(type(loop_departure_time), j) = dict
        for loop_section in loop_departure_time['sections']: #date_time of each section = gare
            #print("departure ",loop_section["departure_date_time"], j)            
            departure_time.append(loop_section["departure_date_time"])
print("departure", departure_time)