import json

import requests

from constants import PASSWORD, USER_NAME, API_BASE_URL, HERO_ENDPOINT
from user_service import validate_user

jwt = validate_user (USER_NAME, PASSWORD)

if jwt is None:
    exit ("Credenciales incorrectas")

heroes_endpoint_url = f'{API_BASE_URL}{HERO_ENDPOINT}'

heroes_response = requests.get (heroes_endpoint_url, headers = {'Authorization': f'Bearer {jwt}'})

if heroes_response.status_code !=200:
    exit (f"Error al obtener la lista de heroes {heroes_response.status_code}")

heroes_data = heroes_response.json ()
print(type(heroes_data))
print(heroes_data)
print(json.dumps(heroes_data, indent=4))