#-------------------------------------
# Python Learning -- Classes & Objects
#-------------------------------------

#-------------------------------------
# Modelling a student and creating a Student Data type

class Student:

     def __init__(self, first_name, last_name, major, gpa, is_on_probation):
         self.first_name = first_name
         self.last_name = last_name
         self.major = major
         self.gpa = gpa
         self.is_on_probabtion = is_on_probation

#-------------------------------------
# Creating a Student object

student_james = Student(first_name="James", last_name="Homes", major="Computer Science", gpa=324, is_on_probation=True)
student_pam = Student(first_name="Pam", last_name="Martins", major="Computer Science", gpa=324, is_on_probation=True)

print(student_james.last_name)
print(student_james.last_name, student_pam.last_name)