#Creating Dictionary in Python
dict1={"id":36,"name":"Harsh","age":21,"marks":(94,84,75)}
print(dict1)

#Using Update Method
dict2={"email":"harsh@mail.com"}
dict1.update(dict2)
print(dict1)

#Using Keys Method
print(dict1.keys())

#Using Values Method
print(dict1.values())

#Using Items Method
print(dict1.items())

#Using Get Method
print(dict1.get("name"))
print(dict1.get("div"))

#using Pop Method
print(dict1.pop("age"))
print(dict1)

#Using Fromkeys Method
dict3={}
dict3.update(dict1.fromkeys(dict1.keys(),"ABCD"))
print(dict3)

#Using Clear Method
dict3.clear()
print(dict3)

#Using Del Keyword
del dict1["email"]
print(dict1)

del dict1
print(dict1)
