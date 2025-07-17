#Creating Set in Python
set1={10,20,30,40}
print(set1)

#Using Add Method
set1.add(50)
print(set1)

#Usinf Copy Method
set2=set1.copy()
print(set2)

#Using Pop Method
set1.pop()
print(set1)

#Using Remove Method
set1.remove(30)
print(set1)

#Using Union Method
print(set2)
print(set1.union(set2))
print(set1|set2)        #'|'(Pipe Operator) can be use as Union

#Using Update Method
set3={95,120,85,43}
set1.update(set3)
print(set1)

#Using Intersection Method
set4={10,2,3}
print(set1.intersection(set4))
print(set1&set4)       #'&'(And Operator) can be use as Intersection

#Using Difference Method
print(set1.difference(set2))
print(set2.difference(set1))
print(set1-set2)       #'-'(Minus Operator) can be use as Difference

#Using Clear Method
set3.clear()
print(set3)

#Using Del Keyword
del set2
print(set2)
