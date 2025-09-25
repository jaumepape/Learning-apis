# Importe del módulo json para formatear y trabajar con datos JSON (Python)
import json

# Importe de la librería requests para hacer solicitudes HTTP (externo)
import requests

# Importe de constantes necesarias desde el archivo constants.py (propio)
from constants import PASSWORD, USER_NAME, API_BASE_URL, HERO_ENDPOINT
# Importe de la función validate_user desde user_service.py (propio)
from user_service import validate_user

# Autentificación del usuario utilizando su nombre de usuario y contraseña
jwt = validate_user (USER_NAME, PASSWORD)

# Si no se obtiene un JWT, las credenciales son incorrectas y se termina la ejecución
if jwt is None:
    exit ("Credenciales incorrectas")

# Construcción de la URL completa para el endpoint de héroes
heroes_endpoint_url = f'{API_BASE_URL}{HERO_ENDPOINT}'

# Realización de una solicitud GET al endpoint de héroes
heroes_response = requests.get (heroes_endpoint_url, headers = {'Authorization': f'Bearer {jwt}'})

# Verificación de sí la respuesta fue exitosa (código 200)
# Si no lo fue, mostramos un mensaje de error y salimos
if heroes_response.status_code !=200:
    exit (f"Error al obtener la lista de heroes {heroes_response.status_code}")

# Si la respuesta fue exitosa, convertimos el contenido JSON en un diccionario de Python
heroes_data = heroes_response.json ()
# Mostramos el tipo de datos que se recibió
print(type(heroes_data))
# Imprimimos los datos sin formato
print(heroes_data)
# Imprimimos los datos de manera legible
print(json.dumps(heroes_data, indent=4))