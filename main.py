import geocoder
import requests


def get_geo():
    g = geocoder.ip('me')
    print(g.latlng)
    return g.latlng

def get_url(geocode):
    url = f'http://wttr.in/{geocode[0]},{geocode[1]}'
    print(url)
    return url

def get_params():
    params = {
        'format': 2,  # погода одной строкой
        'M': ''  # скорость ветра в "м/с"
    }
    return params

def weather():
    return requests.get(get_url(get_geo()), params=get_params())

print(weather())