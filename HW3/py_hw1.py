print("Hello World")

a = "some rubbish text"
b = 100
c = 99.15
d = "here"
e = "is"

c = str(c)

#concatenate method
full_string_concatenate = d + " " + e + " " + a + " " + c[0:2]
print(full_string_concatenate)

#format method
full_string_with_format = "{} {} {} {}".format(d, e, a, c[0:2])
print(full_string_with_format)

#list
list1 = [1, 2, 3]
dict1 = {
    "user": "active",
    "verification": True,
    "list2": ["junior", "advanced", "senior"]
        }
main_list = [4, False, "NEWBES ABOUND", list1, dict1]
print(main_list)

#elements
print(main_list[1])
print(list1[2])
print(dict1["user"])
print(dict1["list2"])

#type changes
num = "123.456"
num = float(num)
print(type(num), num)

num2 = 93735
print(type(num2), num2)
num2 = float(num2)
print(type(num2), num2)
num2 = str(num2)
print(type(num2), num2)