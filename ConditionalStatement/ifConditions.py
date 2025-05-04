import random
age = 19
if age >= 18:
    print("your eligible to vote")
    print("abcd")
    print("xyz")
else:
    print("your not eligible to vote")


if age%2 == 0:
    print("Even number")
else:
    print("odd number")

'''
AND--

A   B     C
0   0     0
0   1     0
1   0     0
1   1     1

OR Gate
A    B     C
0    0     0
0    1     1
1    0     1
1    1     1

'''

char = '@'

if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("vowel")
else:
    print("consonant")

if char.isupper():
    print(char+" is upper case")
    if char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        print("vowel")
    else:
        print("consonant")

elif char.islower():
    print(char+" lower case")
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print("vowel")
    else:
        print("consonant")
else:
    print("it is not upper or lover")

name = "Prathiba Arumugam"
for n in name:
    if n.isupper():
        print(n+" is Upper case")
    else:
        print(n+" is lower case")
             # start, stop, step
for i in range(5,101, 5):
    print(i)

while True:
    if age <=10:
        print("age is lesser than 10")
        break
    

rand = random.randint(1,100)
user_guess = int(input("guess the number:"))
print(rand)


