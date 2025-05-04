from OOPs.ObjectOriantedProgramming import Display


class classA:
    #class level variable
    class_variable = "class Variable"
    @classmethod
    def class_method(cls):
        print("class Method")

classA.class_method()
print(classA.class_variable)
dp = Display()
dp1 = Display()
dp2 = Display()
dp3 = Display()