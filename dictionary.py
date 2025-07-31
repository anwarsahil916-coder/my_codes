stu_det = {'John' : 45,'Bob':58,'Alice': 87}
try:
    name = input("Enter the name of student: ")
    if name in stu_det:
        print("\nStudent and their marks is:", name, "-", stu_det[name])
    else:
        raise KeyError("Student not found.")
except KeyError as e:
    print(e)
else:
    print("\n\nStudent record found.")