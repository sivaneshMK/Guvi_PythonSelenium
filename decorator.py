'''
Decorator
---------
the decorators in python is a function that takes another function a  input, adds some extra
functionality to it and return it --> without modifing the original functionality

Wrapping a normal gift (function) with beautiful gift paper(extra functionality) --> the gift inside remains the same


'''

def decorator_function(original_function):
    def wrapper_function():
        print("wrapper: befor the original function runs")
        original_function()
        print("wrapper: after the original function  runs")
    return wrapper_function

def say_hello():
    print("hello")

decorator = decorator_function(say_hello)
decorator()

@decorator_function
def byeee():
    print("good Byeee")

byeee()


def brush_your_teeth(function):
    def brush():
        print("after wakeup we have to brush our teeth")
        function()
    return brush

@brush_your_teeth
def breakfirst():
    print("eat idly")

breakfirst()