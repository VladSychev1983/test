import requests
import bs4

response = requests.get("https://www.iplocation.net")
html_data = response.text
soup = bs4.BeautifulSoup(html_data, features="lxml")

tag = soup.find(name="span",class_="table-ip4-home")

ip_address = tag.text

ip_address = ip_address.strip()

print(ip_address)



