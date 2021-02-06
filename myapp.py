import requests
import json

URL = "http://localhost:8000/studentinfo/"

def get_data(id=None):
    data ={}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)

#get_data()

def post_data():
    data = {'name':'ramesh', 'roll':199,'city':'bajajnagr'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, data=json_data)
    data = r.json()
    print(data)

#post_data()


def update_post():
    data = {
        'id': 6,
        'name':'rahu',
        'city':'parahd'
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data= json_data)
    data = r.json()
    print(data)

update_post()


def deleted_post():
    data = {'id':2}
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data=json_data)
    data = r.json()
    print(data)

#deleted_post()