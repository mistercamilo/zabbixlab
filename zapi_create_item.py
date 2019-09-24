import requests, json, sys

headers = {'Content-Type': 'application/json'}
endpoint = 'http://localhost:8080'

with open('auth.json', 'r') as f:
    zauth = json.load(f)

r = requests.post('{}/zabbix/api_jsonrpc.php'.format(endpoint), data=json.dumps(zauth),  headers=headers)
auth = json.loads(r.content)["result"]


with open(sys.argv[1], 'r') as f:
    jsonfile = json.load(f)

jsonfile["auth"] = auth

r = requests.post('{}/zabbix/api_jsonrpc.php'.format(endpoint), data=json.dumps(jsonfile),  headers=headers)

data = json.loads(r.content)

print(json.dumps(data))