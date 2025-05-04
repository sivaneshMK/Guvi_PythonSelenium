# declare a method
# def add():
#     print(1+2)
from OOPs import StaticMethodProgramming


# declaring method with arguments
# arg: a and b

def add(a, b):
    print(a+b)
    return a+b


def sub(a, b):
    print(a-b)

# to call a method
total = add(9, 6)
print(total)
add(8, 22)
add(99, 33)
sub(6, 6)
sub(9, 6)


# add 5 number take avg of 5 number

def add_all_values_from_list(marks):
    total = 0
    for mark in marks:
        total = total+mark
    return total


def avg(total, no_of_values):

    return total/no_of_values


def std_avg_mark(marks):
    total = add_all_values_from_list(marks)

    std_avg = avg(total, len(marks))
    return std_avg

rajesh = [65, 83, 70, 60, 90]
rajesh_avg = std_avg_mark(rajesh)
print(rajesh_avg)



# call back function

def greet(name):
    print(f"Hello {name}")

def process_user(callback):
    user_name = 'Ashnet'
    callback(user_name)

process_user(greet)

StaticMethodProgramming.classB.static_method()
