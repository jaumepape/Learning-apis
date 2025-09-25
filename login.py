# Importe de la librería requests para realizar peticiones HTTP (externo)
import requests


def validate_user (user_name, password):
    # Creación de un diccionario con los datos de usuario y contraseña
    user_data = dict (UserName = user_name, Password = password)
    # URL del endpoint de autenticación
    auth_url = "https://heroes.vdata.net/api/Authentication/Authenticate"
    # Realización de una solicitud POST enviando los datos como JSON
    response = requests.post (auth_url, json = user_data)
    # Si la respuesta es exitosa (código de estado 200), devuelve el texto de la respuesta
    if response.status_code == 200:
        return response.text
    else:
        # Si no es exitosa, devuelve None
        return None

# Solicitación al usuario para que ingrese su nombre de usuario y contraseña
user_name_input = input ("Ingrese su usuario: ")
password_input = input ("Ingrese su contraseña: ")

# Llama a la función para validar las credenciales del usuario
jwt = validate_user (user_name_input, password_input)
# Si las credenciales no son válidas se termina la ejecución del programa
if jwt is None:
    exit ("Credenciales incorrectas")
# Si las credenciales son correctas, muestra un mensaje de bienvenida y el JWT recibido
print ("Bienvenido al sistema")
print (jwt)