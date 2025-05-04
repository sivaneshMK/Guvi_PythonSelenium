'''
creating relationship between 2 or more classes and transffering
properties from one class to another class

the relation ship is called as IS-A Relationship


1. single inheritance--> parent--> child
2. multi level inheritance--> parent--> child--> grandchild
3. hierarchical inheritance--> parent
                                1. child1
                                2. child2
4. multiple inheritance --> parent1, parent2--> child

5. hybrid inheritance --> combination of 2 or more inheritance

Method Overriding--> used to archive run time polymorphism
------------------
if parent and child have same properties that means have same method and same parameter type and list
then the parent class method will get overrided by the child class method
in runtime
is called as method overriding

'''
from OOPs.Encapsulation import __parent


class Prakash:

    def tailor(self):
        print("Garments owner")

    def farming_land(self):
        print("1.5 acrs")

    def chef(self):
        print("Prakash chef")

class Bhanumathi:

    def home_maker(self):
        print("Banumathi Home_maker")

    def chef(self):
        print("continentel chef")

class Santhosh(Bhanumathi, Prakash):
    def flat(self):
        print("2BHK")

    def car(self):
        print("Lambokini")

class Divya(Prakash, Bhanumathi):
    def home_maker(self):
        print("Divya Home_maker")

santhosh_obj = Santhosh()
santhosh_obj.flat()
santhosh_obj.car()
santhosh_obj.tailor()
santhosh_obj.farming_land()
santhosh_obj.chef()
santhosh_obj.home_maker()

divya_obj = Divya()
divya_obj.farming_land()
divya_obj.tailor()
divya_obj.home_maker()
divya_obj.chef()


