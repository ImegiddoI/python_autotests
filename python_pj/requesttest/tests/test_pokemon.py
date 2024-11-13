import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3e22be39fa32eb5bc9ffc399db181e86'
HEADER = {'Content-Type':'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '8363'


def test_status_code_trainers():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_name():
    response_trnr_nm = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_trnr_nm.json()["data"][0]["trainer_name"] == 'карапуз'

