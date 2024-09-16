from encodings import normalize_encoding
from unidecode import unidecode



def format_city(city): 
    normalized_city =unidecode(city).strip().title()
    return normalized_city

def get_city_latitude(city): 
    #Get the latitude and latitude
    latitude = test_list[city]['latitude']
    return latitude

def get_city_longitude(city): 
    #Get the latitude and latitude
    longitude = test_list[city]['longitude']
    return longitude
    
    







test_list = {
    "Brasília": {"latitude": -15.793889, "longitude": -47.882778},
    "São Paulo": {"latitude": -23.550520, "longitude": -46.633308},
    "Rio de Janeiro": {"latitude": -22.906847, "longitude": -43.172897},
    "Belo Horizonte": {"latitude": -19.924501, "longitude": -43.935237},
    "Salvador": {"latitude": -12.971399, "longitude": -38.501392},
    "Fortaleza": {"latitude": -3.717220, "longitude": -38.543369},
    "Recife": {"latitude": -8.047562, "longitude": -34.877001},
    "Porto Alegre": {"latitude": -30.034647, "longitude": -51.217658},
    "Curitiba": {"latitude": -25.428954, "longitude": -49.267137},
    "Manaus": {"latitude": -3.119028, "longitude": -60.021731},
    "Belém": {"latitude": -1.455833, "longitude": -48.504444},
    "Goiânia": {"latitude": -16.686891, "longitude": -49.264794},
    "Florianópolis": {"latitude": -27.595377, "longitude": -48.548050},
    "São Luís": {"latitude": -2.530730, "longitude": -44.306820},
    "Maceió": {"latitude": -9.665899, "longitude": -35.735000},
    "Natal": {"latitude": -5.794480, "longitude": -35.211000},
    "Aracaju": {"latitude": -10.947246, "longitude": -37.073082},
    "João Pessoa": {"latitude": -7.119495, "longitude": -34.845011},
    "Cuiabá": {"latitude": -15.601410, "longitude": -56.097891},
    "Campo Grande": {"latitude": -20.469710, "longitude": -54.620121},
    "Palmas": {"latitude": -10.249091, "longitude": -48.324285}
}



