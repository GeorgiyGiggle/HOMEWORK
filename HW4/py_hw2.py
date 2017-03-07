dict1 = {
    "first_name": "Donald",
    "last_name": "Trump",
    "email": "donaldtrump@gmail.com",
    "age": 39
}

a = []

for key in dict1:
    if(type(dict1[key]) == str and len(dict1[key]) > 5):
        print(dict1[key]), a.append(dict1[key])
    if(type(dict1[key]) == int and dict1[key] in range(25, 40)):
        print(dict1[key]), a.append(dict1[key])

print("More than 5 symbols for strings and range 25-40 for int:", a)


for element in a:
    if type(element) == str and element.find("r") and element.find("m"):
        a.remove(element), print("Removed words with letters 'R' and 'M':", a)