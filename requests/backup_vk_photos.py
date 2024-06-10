"""
Программа для резервного копирования фотографий VK в Яндекс Диск.
Итоговая работа по программе Netology Python OOP
"""
import requests
from pprint import pprint
import os
import re
import time as t
from datetime import datetime, date, time
import json

VK_API_KEY=""
VK_USER_ID =""

YA_API_KEY=""

class VK:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}
 
    def get_photos(self):
        photos_dict = {}
        params = {'owner_id': self.id, 'album_id':'profile', 'rev' : '0', 'photo_size': '1','extended':'1'}
        url = 'https://api.vk.com/method/photos.get'
        response = requests.get(url, params={**self.params,**params})
        items_list = response.json()["response"]["items"]
        for x in items_list:
            filename = str(x["likes"]["count"]) + '_' + str(x["date"]) + '.' + 'jpg'
            photos_dict[filename] = x["sizes"][-1]["url"]
        self.download_photos(photos_dict)
    
    def download_photos(self, photos_dict):
        if len(photos_dict) > 0:
            path_to_dir = self.create_dir()
            for filename,url in photos_dict.items():
                print("Downloading",filename, end=' ')
                response = requests.get(url, allow_redirects=True)
                path = path_to_dir + '\\' + filename
                with open (path,"wb") as f:
                    f.write(response.content)
                t.sleep(2)
                if os.path.isfile(path):
                    self.log(filename)
                    print("Ok!")
        else:
            print("Nothing download!\n")
    
    def create_dir(self):
        mydir = 'vk_images'
        current_directory = os.getcwd()
        path_to_dir = current_directory + '\\' + mydir
        if not os.path.isdir(path_to_dir):
            os.makedirs(path_to_dir)
        return path_to_dir

    def log(self,filename):
        with open("download_vk.json","a") as f:
            f.write('[{\n')
            f.write(f'"file_name": {filename},\n')
            f.write(f'"size": "z"\n')
            f.write('}]\n')

class YA_DISK:
    def __init__(self,api_key):
        self.token = api_key
        self.headers = {'Authorization': f'OAuth {self.token}'}
        self.dirname = 'VK-PHOTOS'
    
    def create_dir(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': self.dirname}
        response = requests.put(url, headers=self.headers, params=params)
        print(response)
        print(response.json())

    def upload_photos(self):
        folder_name = 'vk_images'
        path = os.getcwd() + '\\' + folder_name + '\\'
        files_list = os.listdir(path)
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        for filename in files_list:
            print(f'Uploading {filename}',end=" ")
            params = {'path': f'{self.dirname}/{filename}'}
            response = requests.get(url, headers=self.headers, params=params)
            url_upload = response.json()["href"]
            path_to_file = os.getcwd() + '\\' + folder_name + '\\' + filename
            with open(path_to_file, "rb") as f:
                requests.put(url_upload, files={'file': f})
            self.log(filename)
            print("Ok!")
            t.sleep(1)

    def log(self,filename):
        with open("upload_yandex.json","a") as f:
            f.write('[{\n')
            f.write(f'"file_name": {filename},\n')
            f.write(f'"size": "z"\n')
            f.write('}]\n')
    
#Download VK Photos
vk = VK(VK_API_KEY,VK_USER_ID)
vk.get_photos()

#Upload to Yandex Disk
ya = YA_DISK(YA_API_KEY)
ya.create_dir()
ya.upload_photos()
