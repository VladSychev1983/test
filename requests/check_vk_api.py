import requests

class VK:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}
        
    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()
    
    def get_status(self):
        url = 'https://api.vk.com/method/status.get'
        #print(headers)
        params = {'user_id': self.id }
        response = requests.get(url, params={**self.params, **params})
        return response.json()
        
    
access_token= ""

private_token = ''

user_id = ''
vk = VK(access_token, user_id)

print(vk.users_info())
print(vk.get_status())

# токен полученный из инструкции
