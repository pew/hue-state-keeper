import requests
import time
import json

user = ""
apiurl = "http://192.168.1.2/api/"+user

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

while deadlamp():
    for l in deadlamp():
        if l['reachable'] == False:
            bri = {"bri":30}
            setBri = requests.put(apiurl+"/lights/"+l['id']+"/state", json=bri)
            time.sleep(2)
        else:
            l.pop['id']
