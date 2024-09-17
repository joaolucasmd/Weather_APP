import requests 
import json




def get_latitude(postal_code): 
    cep = str(postal_code)
    info = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
    info = info.json()
    latitude = info['lat']
    return latitude


def get_longitude(postal_code): 
    cep = str(postal_code)
    info = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
    info = info.json()
    longitude = info['lng']
    return longitude




def get_city_name(postal_code): 
    cep = str(postal_code)
    info = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
    info = info.json()
    city = info['city']
    return city






 
