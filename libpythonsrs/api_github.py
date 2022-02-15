import requests

def buscar_avatar(usuario):

    """
    :param usuario:
    :return:
    """
    url = f'http://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']

print(buscar_avatar('Cicerosoares'))