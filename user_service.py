import requests

from constants import API_BASE_URL, AUTHENTICATION_ENDPOINT


def validate_user (user_name, password):
    user_data = dict (UserName = user_name, Password = password)
    auth_url = f'{API_BASE_URL}{AUTHENTICATION_ENDPOINT}'
    response = requests.post (auth_url, json = user_data)
    if response.status_code == 200:
        return response.text
    else:
        return None
