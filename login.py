import requests

def validate_user (user_name, password):
    user_data = dict (UserName = user_name, Password = password)
    auth_url = "https://heroes.vdata.net/api/Authentication/Authenticate"
    response = requests.post (auth_url, json = user_data)
    if response.status_code == 200:
        return response.text
    else:
        return None

user_name = input ("Ingrese su usuario: ")
password = input ("Ingrese su contraseña: ")

if validate_user(user_name, password) is not None:
    print ("Bienvenido al sistema")
    print (validate_user(user_name, password))
else:
    print ("Credenciales incorrectas")