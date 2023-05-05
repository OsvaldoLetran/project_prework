import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') # direccion hacia donde queremos hacer la solicitud
    print(r.status_code)     #obtenemos el estado en http o https
    print(r.text)     # cual es el retorno o que info da el API
    print(type(r.text))    # obtenemos que es un str
    categories = r.json()    # formato json lo transforma en una lista que puede iterar python
    for category in categories:
        print(category['name'])