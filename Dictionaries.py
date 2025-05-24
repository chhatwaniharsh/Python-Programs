'''demo1 = { "name": "Harsh", "Course": "Python", "age": 21 }
print(demo1)

demo2 = dict(name = "Harsh", age = 21, city= "Jalgaon")
print(demo2["name"])

demo1["Course"]="Java"
print(demo1)

demo3={"Degree":"BCA"}
demo1.update(demo3)
print(demo1)

'''

demo1 = { "name": "Harsh", "Course": "Python", "age": 21 }
print(demo1)
del demo1["Course"]
print(demo1)
del demo1
print(demo1)
