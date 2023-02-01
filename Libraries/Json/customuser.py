import json
from json import JSONEncoder


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Mirshod", 24)


# encoding with function
def encode_user(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError("Object is not Json serializable")


# userJson = json.dumps(user, default=encode_user)
# print(userJson)


# encoding with class
class UserEncode(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


user_next_json_encoder = json.dumps(user, cls=UserEncode)
print(user_next_json_encoder)


# convert json to User class of instance
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct


class_instance_user = json.loads(user_next_json_encoder, object_hook=decode_user)
print(type(class_instance_user))
print(class_instance_user.name)