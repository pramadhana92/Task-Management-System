# -*- coding: utf-8 -*-

import json
import requests

url_list = "http://localhost:8000/tasks/api"
url_detail = "http://localhost:8000/tasks/api/"

# add several data
requests.post(url_list, {"id":101, "title":"Tugas Matematika","description":"Mengerjakan buku halaman 10-13"})
requests.post(url_list, {"id":102, "title":"Tugas dari Ibu","description":"Menyapu teras rumah"})
requests.post(url_list, {"id":103, "title":"Tugas Pribadi","description":"Membaca buku algoritma"})
requests.post(url_list, {"id":104, "title":"Tugas Pribadi 2","description":"Membereskan kamar"})

# list data
response = requests.get(url_list)
print(response.json())

# update data
requests.put(url_detail + "101/", data={"title":"Tugas Bahasa Inggris"})
requests.put(url_detail + "102/", data={"is_complete":True})

# detail data
response = requests.put(url_detail + "101/")
print(response.json())
response = requests.put(url_detail + "102/")
print(response.json())

# delete data
response = requests.delete(url_detail  + "103/")
response = requests.get(url_list)
print(response.json())