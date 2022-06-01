import requests as r
import json as j


class endpoints:
    url = 'https://dog.ceo/api'
    get_all = '/breeds/list/all'
    get_by_breed =  '/breed/<breed>/images'
    get_random_image = '/breeds/image/random'

def get(url):
    return r.get(url).json()['message']

def get_all_breeds():
    res = get(endpoints.url+endpoints.get_all)

    breeds= []
    for b in res:
        breeds += [b]

    return breeds

def get_images_by_breed(breed):
    res = get(endpoints.url + endpoints.get_by_breed.replace('<breed>',breed))

    images = []
    for image in res:
        images += [image]

    return images

def get_random_image():
    res = get(endpoints.url + endpoints.get_random_image)

    return res

