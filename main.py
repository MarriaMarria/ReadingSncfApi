from read_api import *

#https://stackoverflow.com/questions/419163/what-does-if-name-main-do

if __name__ == '__main__':

    logging.basicConfig(filename = "info_sncf.log", 
    level= logging.INFO, 
    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')
    logging.info('Request api -- start')


    my_class = ReadingSncfApi()
    my_class.request_JSON()
    my_class.my_endpoints()
    #print(my_class.my_endpoints_list)
    my_class.my_id()
    my_class.my_station_name()
    my_class.my_coord()
    #print(my_class.my_list_coord) #print pour afficher valeur
    my_class.csv_station()
    my_class.csv_endpoints()
    my_class.request_api_paris_lyon()
    my_class.save_my_paris_lyon_json()
    my_class.nbr_of_train_change()
    #print(my_class.transfers_list)
    my_class.collectiong_station_name()
    #print(my_class.stop_list)
    #print(my_class.stop_time)
