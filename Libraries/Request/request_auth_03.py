import requests
# Working authentication with request


res = requests.get("https://httpbin.org/basic-auth/Mirshod/test123", auth=("Mirshod", "test123"))

print(res.text)
print(res.status_code)
print(res.url)

print()

# timeout
res = requests.get("https://httpbin.org/#/Dynamic_data/get_delay__delay_/delay/3/", timeout=3)
print("\t\t.....Timeout.....")
print(res)