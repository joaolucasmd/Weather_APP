import cities_location as cities_location  
import requests 
import json 

city = input('Informe a cidade: ')

latitude = cities_location.get_city_latitude(city)
longitude = cities_location.get_city_longitude(city)

TOMORROW_API_KEY = 'HJyGH4bk5U3tvCYwZOYFOV7E3y6Jx2U2'
url = f"https://api.tomorrow.io/v4/weather/realtime?location={latitude},{longitude}&apikey={TOMORROW_API_KEY}"

headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)

##Se o erro code é 200 a requisição foi bem sucedida
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f'Erro na requisição: {response.status_code}, mensagem: {response.json().get("message", "")}')



    
