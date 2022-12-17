class Student:
    def __init__(self, name, age) -> None:
        # self.name & self.age are Instance variable [ https://pynative.com/python-instance-variables/ ]
        self.name = name
        self.age = age

s = Student('Samiul', 32)
print(s.name)

s1 = Student('Sami', 32)
print(s1.name)


class Teacher:
    def __init__(self, name, subject) -> None:
        self.name = name
        self.subject = subject

    # Instance method that is accessing instance variable
    def display(self):
        print(t.subject)

t = Teacher('Saddam', 'ICT')
t.display()