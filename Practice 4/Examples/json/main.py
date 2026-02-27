import json

with open("sample-data.json") as input_file:
    data = json.loads(input_file.read())

if not data:
    quit()

parsed_data = []

for i in range(len(data["imdata"])):
    obj = data["imdata"][i]["l1PhysIf"]["attributes"]
    d = {}
    d["dn"] = obj["dn"]
    d["speed"] = obj["speed"]
    d["descr"] = obj["descr"]
    d["mtu"] = obj["mtu"]
    parsed_data.append(d)

print("""Interface Status
=======================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

for i in parsed_data:
    print(f"{i['dn']:51}{i['descr']:21}{i['speed']:10}{i['mtu']:6}")

