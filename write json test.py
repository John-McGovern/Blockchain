"""
when updating json, first open it with the open function and save to a variable,
then use the update function to add extra data to that variable,
then overwrite the old json with the new data.

"""


import json

test_json ={
    "hey": "you"}

"""
second_json ={
    "help": "me",
    "right":"now",
    "I think": "he has"}
"""

second_json ={ "good" :{
    "help": "me",
    "right":"now",
    "I think": "he has"}}

with open("test.json", 'w') as json.file:
    json.dump(test_json, json.file)

with open("test.json") as readable:
    add_to = json.load(readable)

#add_to["help"]= "me"

add_to.update(second_json)


with open("test.json", 'w') as json.file:
    json.dump(add_to, json.file)

#have to load keep file as variable, update variable with new file and then overwrite file with new variable

#y = json.load("test.json")

#with open("test.json", 'w') as json.file:
    #json.dump(second_json, json.file)



with open("test.json") as readable:
    message = json.load(readable)
"""
for key, value in message.items():
    print(key, value)
    #print(key)
"""

with open("online.json") as readable:
    message = json.load(readable)
    print(message)


# <input id="To" type="text" name="to" value="">

"""
<form action="/" method="post">
<label for="user_page">User:</label>
<select name="user_page">
{% for user in users%}
<option value="{{user}}">{{user}}</option>
{%endfor%}
</select>
<br>
<br>
<input type="submit" name="user_page" value="submit">
</form>
"""
