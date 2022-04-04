MyList = ["C", "C++", "Java", "Python"]
print("Initial list : ",MyList)

MyList.append("Javascript")
print("List after appending : ",MyList)

MyList.clear()
print("List after clearing : ",MyList)

MyList.append("C")
MyList.append("C++")
MyList.append("Java")
MyList.append("Python")
print("List after appending to initial :",MyList)

print("No. of elements in Java :",MyList.count("Java"))

MyExtend = ["CAD", "CAM"]
MyList.extend(MyExtend)
print("Extended List : ",MyList)

print("Index of Python : ",MyList.index("Python"))

MyList.insert(1, "C#")
print("List after inserting : ",MyList)

MyList.pop(1)
print("List after popping : ",MyList)

MyList.remove("CAD")
MyList.remove("CAM")
print("List after removing : ",MyList)

MyList.reverse()
print("Reverse List : ",MyList)

MyList.sort()
print("Sorted List : ",MyList)
