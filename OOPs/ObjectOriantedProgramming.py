
class Display():

    # constructor of a class
    def __init__(self):
        print("This is Display class Constructor")
        # instance variable
        self.Voltage = "230v"
        self.Current = "5A"
        # local variable--> can be declared inside the method but it can't be accessed outside of the method
        resistance = "44R"
        print(resistance)
    #instance method or object level method
    # instance methods can be accessed by using object only
    def lcd(self):
        print("it is lcd display")

    def speaker(self):
        print("in-build speaker")

# while creating an object you have to call any one constructor
# of class
# constructor is don't have special name like method so
# class name can be used for constructor as well
# object name = class constructor()
# if your not creating any constructor then the compiler will
# create constructor for a class in compile time
# this is called as default constructor
# if you want to create a constructor def __init__():
# While creating an object the constructor will construct
# instance content of a class and it will return where we creating an object
# constructor is called implicitly when we creating an object
# that means we no need to call a constructor like a method
lg = Display()
lg.lcd()
lg.speaker()
print(lg.Current)
print(lg.Voltage)
#print(lg.resistance)

