import requests

r = requests.get('https://xkcd.com/53/')

# print(help(r))
# print(r.text)
# print(f"status code: {r.status_code}")
# print(f"Encoding: {r.encoding}")
# checking headers
# print(r.headers)


# get image from a website
image = requests.get("https://imgs.xkcd.com/comics/hobby.jpg")
# print(image.content)
# with open("hobby.jpg", "wb") as f:
#     f.write(image.content)


payload = {"page": 2, "count": 30}
res = requests.get("https://httpbin.org/get", params=payload)
print(res.text)
print(res.url)
