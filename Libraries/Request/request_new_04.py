from json import JSONEncoder, JSONDecodeError

import requests
import json

url = "https://kun.uz/"

r = requests.get(url)


# if r.headers.get('content-type') == 'application/json':
#     print("true")
#     print(r.headers.get('content-type'))
# else:
#     print("false")
#     print(r.headers.get('content-type'))

# try:
#     # json_data = r.json()
#     # print(json_data)
#     js_data = json.dumps(r.text, indent=5)
#     js_to_dict = json.loads(js_data)
#     print("Data is serialized")
#     print(type(js_to_dict))
#
# except JSONDecodeError:
#     print("Data is not serialized")
