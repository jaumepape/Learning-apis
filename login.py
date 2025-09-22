def validate_user (user_name, password):
    user_data = dict (UserName = user_name, Password = password)
    return True

user_name = input ("Ingrese su usuario: ")
password = input ("Ingrese su contraseña: ")

print (validate_user(user_name, password))