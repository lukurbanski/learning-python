import json
import requests

json_example = """
{"widget": {
    "debug": "on",
    "window": {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width": 500,
        "height": 500
    },
    "image": { 
        "src": "Images/Sun.png",
        "name": "sun1",
        "hOffset": 250,
        "vOffset": 250,
        "alignment": "center"
    },
    "text": {
        "data": "Click Here",
        "size": 36,
        "style": "bold",
        "name": "text1",
        "hOffset": 250,
        "vOffset": 100,
        "alignment": "center",
        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
    }
}}
"""

jsonload = json.loads(json_example)

lst = []
lst.append(jsonload["widget"]["window"]["title"])
lst.append(jsonload["widget"]["image"]["src"])
lst.append(jsonload["widget"]["text"]["data"])


r = requests.get('https://jsonplaceholder.typicode.com/todos')

jsonload = json.loads(r.text)

# print(jsonload)

for j in jsonload:
    if j["id"] <= 10:
        print('Title -->',j["title"])
