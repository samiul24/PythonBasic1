class Student:
    def __init__(self, name, age) -> None:
        # self.name & self.age are Instance variable [ https://pynative.com/python-instance-variables/ ]
        self.name = name
        self.age = age

s = Student('Samiul', 32)
print(s.name)

s1 = Student('Sami', 32)
s1.dob = 1992 # add new instance variable 
print(f"Name: {s1.name}, Age: {s1.age}, DOB: {s1.dob}")


class Teacher:
    def __init__(self, name, subject) -> None:
        self.name = name
        self.subject = subject

    # Instance method that is accessing instance variable
    def display(self):
        print(t.subject)

t = Teacher('Saddam', 'ICT')
t.display()


class Student1:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student1("Jessa", 20)

print('Before')
print('Name:', stud.name, 'Age:', stud.age)

# modify instance variable
stud.name = 'Emma'
stud.age = 15

print('After')
print('Name:', stud.name, 'Age:', stud.age)