import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3e22be39fa32eb5bc9ffc399db181e86'
HEADER = {'Content-Type':'application/json', 'trainer_token' : TOKEN}
body_create = {"name": "generate", "photo_id": -1}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
print(response_create.status_code)

pokemon_id = response_create.json()['id']
print("ИД покемона:", pokemon_id)


body_chg_nm = {"pokemon_id": pokemon_id ,"name": "changed"}

response_chg_nm = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_chg_nm)
print(response_chg_nm.text)
print(response_chg_nm.status_code)


body_catch_pb = {"pokemon_id": pokemon_id}

response_catch_pb = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch_pb)
print(response_catch_pb.text)
print(response_catch_pb.status_code)
