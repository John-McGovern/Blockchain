import json

test_json ={
    "hey": "you"}


second_json ={
    "help": "me"}

with open("test.json", 'w') as json.file:
    json.dump(test_json, json.file)


y = json.load("test.json")

with open("test.json", 'a') as json.file:
    json.update(second_json, json.file)


with open("test.json") as readable:
    message = json.load(readable)

for value, key in message.items():
    print(value)
    print(key)