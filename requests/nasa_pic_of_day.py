"""
Программа для загрузки картинки ДНЯ из NASA.
"""
import requests
import os
from datetime import datetime, date, time

images_dir = 'nasa_images'
url = 'https://api.nasa.gov/planetary/apod'
api_key = ''

def create_dir(dir):
    current_directory = os.getcwd()
    if not os.path.isdir(current_directory +'/' + dir):
        os.makedirs(current_directory +'/' + dir)
    path = current_directory +'\\' + dir
    return path

def get_photo(url,api_key):
    params = {'api_key':api_key}
    response = requests.get(url, params=params)
    print(response.json())
    hdurl = response.json()["hdurl"]
    download_picture(hdurl,params)

def day_today():
    time_now = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}'
    return time_now

def download_picture(hdurl,params):
    response = requests.get(hdurl, params)
    theday = day_today()
    original_file = hdurl.split('/')[-1]
    filename = theday + '_' + original_file
    path = create_dir(images_dir) + '\\' + filename
    print(path)
    with open(path, "wb") as f:
         f.write(response.content)

create_dir(images_dir)
get_photo(url,api_key)