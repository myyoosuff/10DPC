#students = ["ali", "ahmed", "sara", "john", "emily"]
#print(students)
#for student in students:
 #   print(student)

items = ["book", "pen", "notebook", "pencil"]
print(items)
for item in items:
        print("checking item:", item)
        
students = {"ali-": 75, "ahmed-": 80, "sara-": 85, "john-": 20, "emily-": 95}
print(students)
for student, mark in students.items():
        if mark >= 40:
            print(student,mark, "-PASSS:")
        else:
                print(student,mark, "-FAIL:")