import json

f = open("MyFile.txt", "w")
msg = "Hello world. I am a Backend Developer"
f.write(msg)
f.close()

with open("MyFile.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        print(f"{l}")

with open("map.py", "r") as f:
    liness = f.readlines()
    print(liness)

data = {"Mirshod":"Python Engineer"}
with open("data.json", "w") as f:
    json.dump(data, f)