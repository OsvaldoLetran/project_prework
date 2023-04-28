import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)     #obtenemos el estado en https
    print(r.text)     # cual es el retorno o que info da el api
    print(type(r.text))
    categories = r.json()    # de formato python a formato json
    for category in categories:
        print(category['name'])