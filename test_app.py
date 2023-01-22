# -----------------first_app gettig data--------------
import requests

url_api = "http://127.0.0.1:8000/get_movie_d/1"

data = requests.get(url = url_api)
print(type(data  ))

data_json = data.json()

print(data_json)
# ------------------------

# ----------------------secound app to create data ----------------
# import requests
# import json
# url_api = "http://127.0.0.1:8000/create_movie/"

# data = {
#     "movie" : "movie5",
#     "character" : "c5",
# }
# json_data = json.dumps(data)

# r = requests.post(url = url_api, data = json_data)

# data = r.json()

# print(data)

# ---------------------------------------------------------
# ----------------------update data--------------------------
import requests 
import json

# url_api = "http://127.0.0.1:8000/get_data/"
url_api = "http://127.0.0.1:8000/crud/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = url_api, data = json_data)
    data = r.json()
    print(data)

get_data()

def post_data():
    data ={
        'movie' : 'godzilla',
        'character' : 'dinosour'
    }
    json_data = json.dumps(data)
    r = requests.post(url=url_api, data = json_data)
    data = r.json()
    print(data)
# post_data()

# ---------------------partial update---------------
def update_data():
    data ={
        'id':1,
        'movie' : 'avengers : infinity war',
        
    }

    json_data = json.dumps(data)
    r = requests.put(url = url_api, data = json_data)
    data = r.json()
    print(data)
# update_data()

# -------------------------------------------
# ---------------complete update---------------
def complete_update_data():
    data ={
        'id':9,
        'movie' : 'spider-man:no way home',
        'character' : 'mischell',
    }

    json_data = json.dumps(data)
    r = requests.put(url = url_api, data = json_data)
    data = r.json()
    print(data)
# complete_update_data(9)
# ------------------------------------
# ----------delete data----------------
def delete_data():
    data = {'id':10}

    json_data = json.dumps(data)
    r = requests.delete(url = url_api, data = json_data)
    data = r.json()
    print(data)
# delete_data()
# ----------------------------- 