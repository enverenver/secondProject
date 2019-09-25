import json

data = '''
[
    {
        "name" : "Enver",
        "tel" : "888888"
    } ,
    {
        "name" : "Nastya",
        "tel" : "777777"
    }
]'''

info = json.loads(data)
print(info)
for item in info:
    print(item)
    print("Name: ", item["name"])
