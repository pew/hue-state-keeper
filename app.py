import requests
import time
import json
import os.path
import sys

try:
    conf = os.path.exists('config.py')
    import config
except:
    user = input('username: ')
    getBri = input('set brightness: ')
    getIp = requests.get("https://www.meethue.com/api/nupnp")
    if getIp.status_code == 200:
        ip = json.loads(getIp.text)[0]['internalipaddress']
    else:
        exit('Could not obtain IP address of bridge.')

    f = open('config.py', 'w')
    f.write("user = "+"\""+user+"\""+"\n"+"ip = "+"\""+ip+"\""+"\n"+"bri = "+getBri) # ?!?!?
    f.close()
    import config

apiurl = "http://"+config.ip+"/api/"+config.user

def savestate():
    lights = []
    req = json.loads(requests.get(apiurl+"/lights").text)
    for k,v in req.items():
        dict = {'id': k, 'state': v['state']}
        lights.append(dict)
    return json.dumps(lights)

def deadlamp():
    deadLamp = []
    for l in json.loads(savestate()):
        if l['state']['reachable'] == False:
            dict = {'id': l['id'], 'reachable': l['state']['reachable'], 'bri': l['state']['bri']}
            deadLamp.append(dict)
    return deadLamp

while True:
    savelamp = []
    for l in deadlamp():
        if l['reachable'] == False:
            dict = {'id': l['id'], 'reachable': l['reachable']}
            savelamp.append(dict)
            #print('dead:', savelamp)
            time.sleep(2)
    for l in savelamp:
        req = json.loads(requests.get(apiurl+"/lights/"+l['id']).text)
        if req['state']['reachable'] == True:
            #print('back on:', l['id'])
            brightness = {"bri":config.bri}
            setBri = requests.put(apiurl+"/lights/"+l['id']+"/state", json=brightness)
