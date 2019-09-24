from pyzabbix import ZabbixAPI

zapi = ZabbixAPI("http://localhost:8080/zabbix")
zapi.login("Admin", "zabbix")
print("Connected to Zabbix API Version %s" % zapi.api_version())

for h in zapi.host.get(output="extend"):
    print(h['hostid'])