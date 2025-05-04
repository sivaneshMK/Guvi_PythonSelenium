
'''
Restricting access of a content from the class --> it archived by
using data hiding

that means the properties wont be accessed in the direct way from a class



'''

class __parent():

    def parent(self):
        print("parent class")


class Student(__parent):
    def __init__(self, name, roll):
        self.__marks = 95
        self.name = name
        self.roll = roll
    def display_info(self):
        print(f"name: {self.name} Roll: {self.roll} Mark: {self.__marks}")

    def get_marks(self):
        return self.__marks

std = Student("Sivanesh", "1234")

std.display_info()
print(std.name)
print(std.roll)
#print(std.__marks)
print(std.get_marks())

pa = __parent()
