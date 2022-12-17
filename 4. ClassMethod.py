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

    # Instance variable change by method
    def age_change(self, new_age):
        self.age = new_age

    @classmethod
    def school_change(cls, new_school):
        cls.school_name = new_school


# Object declare of Student class
s = Student('Samiul', 32)
#Instance method call
s.show()


print('After changing the instance & class variable')
# Change Instance variable direct
s.name = 'Saddam'
# Change Instance variable by method call
s.age_change(43)
s.school_change('XYZ')

s.show()
