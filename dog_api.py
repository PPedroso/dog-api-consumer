import requests as r
import json as j


url = 'https://dog.ceo/api/breeds'
get_all = '/list/all'

def get_all_breeds():
    res = r.get(url+get_all).json()['message']

    breeds= []
    for b in res:
        breeds += [b]

    return breeds
