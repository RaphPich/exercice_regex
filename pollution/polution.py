import re
from xml.sax.handler import feature_namespace_prefixes

def get_most_polutate():
    with open("moy_tot_quantif_2012.csv") as file :
        lfiles_lines = file.readlines()


    dict_station = {}
    for line in lfiles_lines[1:]:
        t_info = re.split(r';', line)
        dict_station[t_info[1]] = t_info[3]

    dict_station = {k: v for k, v in sorted(dict_station.items(), key=lambda item: item[1])}


    most_poluted = dict_station.popitem()

    with open("stations.csv") as file :
        stations_list = file.readlines()

    my_reg = r""+most_poluted[0]

    for station in stations_list:
        if re.search(my_reg, station):
            city = station.split(";")[2]

    return city


