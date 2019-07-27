import io, os, sys, requests

from PIL import Image
from picamera import PiCamera
from time import sleep

_url = 'cogsvcs api endpoint goes here'
_key = 'your api key goes here'
_maxNumRetries = 10

def processRequest (json, data, headers, params):
    retries = 0
    result = None
    while True:
        response = requests.request('post', _url, json = json, data = data, headers = headers, params = params)
        if response.status_code == 429:
            print("Message: %s" % (respons.json()['error']['message']))
            if retries <= _masNumRetries:
                time.sleep(1)
                retries += 1
                continue
            else:
                print('Error: failed after retrying!')
                break
        elif response.status_code == 200 or response.status_code == 201:
            print(response.status_code)
            if 'content-length' in response.headers and int(response.headers['content-length'])==0:
                print("content-length == 0")
                result = None
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str):
                if 'application/json' in response.headers['content-type'].lower():
                    result = response.json() if response.content else None
                elif 'image' in response.headers['content-type'].lower():
                    result = response.content
        else:
            print("Error code: %d" % (response.status_code))
            print("Message: %s" % (response.json()['error']['message']))
        break
    return result
    

camera = PiCamera()


camera.rotation = 270
camera.start_preview()
sleep(2)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()               

json = None

data = open('/home/pi/Desktop/image.jpg', 'rb').read()

headers = dict()
headers['Ocp-Apim-Subscription-Key'] = _key
headers['Content-Type'] = 'application/octet-stream'

params = { 'visualFeatures' : 'Color,Categories,Tags,Description' } 

result = processRequest(json, data, headers, params)

print(result['tags'])

for index in range(len(result['tags'])):
    if result['tags'][index]['name'] == 'drink':
        print("signalling")
        data = {'args':'1','access_token':'access token goes here'}
        headers={'content-type':'application/x-www-form-urlencoded'}
        _sparkUrl = 'particle device trigger goes here'
        requests.request('post', _sparkUrl, data = data, headers=headers)
    else:
        print("no signal")
