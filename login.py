import requests

def validate_user (user_name, password):
    user_data = dict (UserName = user_name, Password = password)
    auth_url = "https://heroes.vdata.net/api/Authentication/Authenticate"
    response = requests.post (auth_url, json = user_data)
    if response.status_code == 200:
        return response.text
    else:
        return None

user_name_input = input ("Ingrese su usuario: ")
password_input = input ("Ingrese su contraseña: ")

jwt = validate_user (user_name_input, password_input)
if jwt is None:
    exit ("Credenciales incorrectas")
print ("Bienvenido al sistema")
print (jwt)