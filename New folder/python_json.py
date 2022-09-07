import json
person = {"name": "Tim", "age": 26, "city": "Boston", "Title": "engineer"}
personj = json.dumps(person, indent=4, sort_keys=True)
print(personj)

# a = tuple([1, 2, 3, 4, 5])
# aj = json.dumps(a, indent=4,)
# print(aj)
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)
    # json.dump(a, file)
p = json.loads(personj)
print(p)
with open('person.json', 'r') as file:
    q = json.load(file)
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
user = User('Tom', 25)

def encodeuser(o):
    if isinstance(o, User):
        return {'name': o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')
from json import JSONEncoder

class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class.__name__:True}
        return JSONEncoder.default(self, o)


uj = json.dumps(user, default=encodeuser, indent=4)
print(uj)
