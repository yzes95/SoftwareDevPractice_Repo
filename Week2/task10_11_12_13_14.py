# task 10
grade = 0
_1stsum = 0
_2ndsum = 0
try:
    for student in range(1, 16, 1):
        grade += float(input(f"Enter Student {student} Grade: "))
        if student == 8:
            _1stsum = grade
        if student == 15:
            _2ndsum = grade - _1stsum
except ValueError:
    pass

print("The total garde is :", grade)

# task 11
# suggestion: we can use list to store the grades then loop over the list to add them up

# task 12:
print(f"Average grade: {grade/15 :0.1f}")

# task 13:
print(f"Average grade for 1st 8: {_1stsum/8 :0.1f}")
print(f"Average grade for last 7: {_2ndsum/7 :0.1f}")

# task 14:
student_dict = {}
student_list = []
student_No = int(input("Enter the number of students you want to operate on : "))
for student in range(1, student_No + 1, 1):
    student_dict["Name"] = input(f"Enter Student {student} Name: ")
    student_dict["Grade"] = float(input(f"Enter Student {student} Grade: "))
    student_list.append({"Name": student_dict["Name"], "Grade": student_dict["Grade"]})

grade = 0
name = 0
print(
    "\n\nPrinting the whole list with highest grade recordedand its relevant student:"
)
for student in student_list:
    print(f"{student["Name"]} Scored : {student["Grade"]}")
    if grade < student["Grade"]:
        grade = student["Grade"]
        name = student["Name"]

print(f"The Student With the Highest Grade of {grade} is : {name}")
