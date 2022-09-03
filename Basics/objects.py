class Student:
    def __init__(self, name1, major1, gpa1):
        self.name = name1
        self.major = major1
        self.gpa = gpa1

    def honours(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

# student1 = Student("mike", "maths", 4)
# student2 = Student("jim", "physics", 5)
# print(student1.name)
# print(student2.major)


# for index in range(3):
#     print(index)
# name = ""
# major=""
# name = input("Enter your name: ")
# major = input("Enter your Major: ")
# gpa= input("Enter your gpa: ")
# student1 = Student(name, major,gpa)
name = ["", "", ""]
major = ["", "", ""]
gpa = [4, 9, 8]


for index in range(3):
    name[index] = input("Enter name")
    major[index] = input("Enter major")
    gpa[index] = float(input("Enter gpa"))

student = [
 Student(name[0], major[0], gpa[0]),
 Student(name[1], major[1], gpa[1]),
 Student(name[2], major[2], gpa[2])
]

# student1 = Student(name[0], major[0], gpa[0])
# student2 = Student(name[1], major[1], gpa[1])
# student3 = Student(name[2], major[2], gpa[2])


print("name \t major\t gpa")
for i in range(3):
    print(name[i] + "  \t" + major[i] + "  \t" + str(gpa[i])+"\t   "+str(student[i].honours()))
print(student[1].name)


class Mystudent:
    My_student = Student("name", "maths", 9)  # my student inherited all the functions of Student
