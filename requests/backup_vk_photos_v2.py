import requests
import json
import time as t
import os
from pprint import pprint
import urllib.parse

VK_API_KEY=""
VK_USER_ID =""

YA_API_KEY=""

class VK:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}
    
    def get_photos_href(self):
        photos_dict = {}
        params = {'owner_id': self.id, 'album_id':'profile', 'rev' : '0', 'photo_size': '1','extended':'1'}
        url = 'https://api.vk.com/method/photos.get'
        response = requests.get(url, params={**self.params,**params})
        items_list = response.json()["response"]["items"]
        for x in items_list:
            filename = str(x["likes"]["count"]) + '_' + str(x["date"]) + '.' + 'jpg'
            photos_dict[x["sizes"][-1]["url"]] = {"file_name":filename, "size": x["sizes"][-1]["type"] }
        return photos_dict

class YA_DISK:
    def __init__(self,api_key,vk_photos):
        self.token = api_key
        self.headers = {'Authorization': f'OAuth {self.token}'}
        self.dirname = 'VK-PHOTOS'
        self.vk_photos = vk_photos

    def create_dir(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': self.dirname}
        response = requests.put(url, headers=self.headers, params=params)
        return response.status_code
    
    def upload_photos(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        upload_log_list = []
        for photo_href,photo_params in vk_photos.items():
            print(f'Uploading {photo_params["file_name"]}',end=" ")
            path = f'{self.dirname}/{photo_params["file_name"]}'
            params = {'path': f'{path}', 'url': photo_href}
            encoded_params = urllib.parse.urlencode(params)
            response = requests.post(url, headers=self.headers, params=encoded_params)
            if response.status_code == 202:
                print('Ok!')
            upload_log_list.append(photo_params)
            t.sleep(1)
        self.log_file(upload_log_list)

    def log_file(self,upload_log_list):
        with open('upload_disk.json', "w") as file:
            json.dump(upload_log_list, file)

#Download VK Photos Links
vk = VK(VK_API_KEY,VK_USER_ID)
vk_photos = vk.get_photos_href()

#Upload photos to YANDEX DISK by HREF.
ya = YA_DISK(YA_API_KEY,vk_photos)
ya.create_dir()
ya.upload_photos()

