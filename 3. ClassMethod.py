class Student:

    #Class variable
    school_name = 'ABC'

    # Constructor
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    # Instance method
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, School: {Student.school_name}")

# Object declare of Student class
s = Student('Samiul', 32)
#Instance method call
s.show()


print('After changing the instance & class variable')
# Change Instance variable
s.name = 'Saddam'
s.age = 33
#Change class variable
Student.school_name = 'XYZ'

s.show()



