import requests

payload = {"username": "Mirshod", "password": "test123"}
res = requests.post("https://httpbin.org/post", data=payload)

print(res.text)
r_dict = res.json()
print(r_dict['form'])
