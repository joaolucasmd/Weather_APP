from get_cep import get_latitude,get_longitude,get_city_name
import streamlit as st 

import requests 
import json 


st.set_page_config(page_title='Temperatura da sua cidade')

st.write('API para exibir a temperatura atual do seu CEP')



cep = st.text_input("Insira o Cep da sua cidade:")  
latitude = get_latitude(cep)
longitude = get_longitude(cep)
city = get_city_name(cep)

TOMORROW_API_KEY = 'HJyGH4bk5U3tvCYwZOYFOV7E3y6Jx2U2'
url = f"https://api.tomorrow.io/v4/weather/realtime?location={latitude},{longitude}&apikey={TOMORROW_API_KEY}"

headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)

##Se o erro code é 200 a requisição foi bem sucedida
if response.status_code == 200:
    data = response.json()
    # print(json.dumps(data, indent=4))
    temp = data['data']['values']['temperature']
    st.write(f'Em {city} essa é a temperatura atual: {temp}')
    # print(data)
else:
    print(f'Erro na requisição: {response.status_code}, mensagem: {response.json().get("message", "")}')




