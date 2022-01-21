import requests
from requests.structures import CaseInsensitiveDict
import time

url = 'http://localhost:4000/login'
myobj = {'username': 'Kylie'}

x = requests.post(url, data = myobj)

auth_token = x.json().get('accessToken')

url = "http://localhost:3000/posts"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer {}".format(auth_token)



def autoGetRequest(maxTime):
    for i in range(1,maxTime):
        time.sleep(1)
        resp = requests.get(url, headers=headers)
        print('Time: {}s, Status Code: {}, Content: {}'.format(i,resp.status_code,resp.content))

autoGetRequest(20)

