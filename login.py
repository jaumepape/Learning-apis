import requests

def validate_user (user_name, password):
    user_data = dict (UserName = user_name, Password = password)
    auth_url = "https://heroes.vdata.net/api/Authentication/Authenticate"
    response = requests.post (auth_url, json = user_data)
    return response.text
user_name = input ("Ingrese su usuario: ")
password = input ("Ingrese su contraseña: ")

print (validate_user(user_name, password))