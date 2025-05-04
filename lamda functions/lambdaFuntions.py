# lambda arguments: expression
from functools import reduce

add = lambda x, y: x+y
print(add(6, 8))

add = lambda z, x, y: z+x+y
print(add(9,6,9))

def add(*args):
    print(args)

add(6, 6, 9, 8, 36, 87,69, 587)
number = [6, 98, 556, 56,8,548,545,548,78,584,54987,89,654]
total  = reduce(lambda a, b: a+b, number)
print(total)

odd_even = lambda a: print("even number")if a % 2 == 0 else print("odd")
odd_even(74)
odd_even(79)

# map funtion applies a function to every idtem in an iterable(list, tuple, ect)
number = [892, 839, 82928, 4423]
result = map(lambda x: x*2, number)
print(result)
print(list(result))

name = "Sivanesh"
out = map(lambda x: x.isupper() , name)
print(list(out))
# filter() is used to  filter out elements based on a condition (return only the elemnets that are true for the funtion)
# it also returns a filter object(again, convert it to a list to see result)
vowel = ['a', 'e', 'i', 'o', 'u']

check_vowel = list(filter(lambda x: x in vowel, name))

print(check_vowel)



l=[2,3,5]
odd=[]
even=[]
odd_even=lambda l: ([print("even",i, even.append(i)) if i%2==0  else print("odd",odd.append(i))  for i in l])
odd_even(l)
print(odd)
print(even)

'''
filter
----------
selects only items matching a condition
output size < = input size(can be smaller) --> picks only vowel

map
-----------
transform every items
output size = input size
example double each number

'''




