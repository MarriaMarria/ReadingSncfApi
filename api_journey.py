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


'''
arrival_time = []

for loop_arrival in journeys:
    #print(len(loop_arrival['sections'])) #list #length = 3
    for loop_section in loop_arrival['sections']:
        arrival_time.append(loop_section["name"])
print("arrival date time of each section", arrival_time)

departure_time = []
for loop_departure in journeys:
    #print(len(loop_departure['sections'])) #list #length = 3
    for loop_section in loop_departure['sections']:
        departure_time.append(loop_section["departure_date_time"])
#print("departure date time of each section", departure_time)

#stop_time = map(lambda x,y: x - y, arrival_time, departure_time)
#print(stop_time)


journeys = data_journey['journeys']
#pprin. pprint(journeys) #=list

pprint.pprint(stations) #c'est une liste

'''
journeys = data_journey["journeys"]
journey = journeys[0]

#print(type(journey)) #dict
########
sections = journey['sections'][0]
#print(sections.keys())

from_departure = sections['from']
print(type(from_departure['embedded_type']))

for key in from_departure.keys():
    print(type(from_departure[key]), key)

## definition of the type of all keys in section
'''
for key in journey.keys():
    print(type(journey[key]), key)

<class 'str'> status
<class 'dict'> distances : {'taxi': 0, 'car': 0, 'walking': 0, 'bike': 0, 'ridesharing': 0}
<class 'list'> links
<class 'list'> tags
<class 'int'> nb_transfers
<class 'dict'> durations : {'taxi': 0, 'walking': 0, 'car': 0, 'ridesharing': 0, 'bike': 0, 'total': 8220}
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
            (<type 'unicode'>, u'embedded_type')
            (<type 'unicode'>, u'id')
            (<type 'int'>, u'quality')
            (<type 'dict'>, u'stop_area')
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

print(journey["sections"][0]['from']['name'])


