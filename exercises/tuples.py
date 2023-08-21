# tuple = collecton which is ordered and unchangeable
# used to group together related data

student = ("Mary", 21, "fem")

print(student.count("Mary"))
print(student.index(21))

for x in student:
    print(x)
    
if("Mary") in student:
    print("Mary is the name of the student")