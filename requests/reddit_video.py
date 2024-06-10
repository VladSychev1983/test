import requests
from pprint import pprint
import re
import time as t
from datetime import datetime, date, time

url = "https://www.reddit.com/r/gifs/top.json?t=day"

response = requests.get(url, timeout=15)
#resp_dict = response.json()
print(response.text)
list_urls = re.findall(r"\"fallback_url\": \"(.+?)\"",response.text)
time_now = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}_'
t.sleep(2)
#print(response.text)
#downloads files
if len(list_urls) > 0:
    for url in list_urls:
        resp = requests.get(url, allow_redirects=True)
        t.sleep(2)
        filename = time_now + url.split("/")[-2] + '.mp4'
        with open(filename,'wb') as f:
            f.write(resp.content)
else:
    print('Empty urls list!\n')