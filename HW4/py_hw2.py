dict1 = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@gmail.com",
    "age": 25
}

a = list(dict1.values())
print(a)

for value in dict1.values():
    if type(value) == str and len(value) > 5:
        if value.find("a") != -1:
            a.append()
    a.append()
