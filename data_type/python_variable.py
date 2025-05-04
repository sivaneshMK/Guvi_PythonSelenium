# Variable
import re
'''
Variables are used to store value
Why we need to store values
if you want to reuse the values throughout the program
we need to store the value in variable

Syntax
variable_name = variable value
x = 10

x=10
y = 20
x+y=? 30


'''

a = 45
print(a)

b = 25

print(a+b)

'''
Numeric   --> int, float, complex
boolean
set
sequence type --> string, list, tuple
dictionary
'''
# int
mobile = 4587965487

# float
tenth_avg_mark = 83.39999999999999999999999999999995465465564656465464
print(tenth_avg_mark)

# complex
# 2+4j

x = 2+4j

print(x)
print(x.imag)
print(x.real)
print(x.conjugate())

name = "Sivanesh"

print(name)
print(name[::-1])
print(name.upper())

trainer = "Sivanesh"

std = 'Devihlsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffauiwyerrrrrrrrrrrrrrrrrrrrrruqiwueriuwyeioryqwoiywiryewiywezsas'

print(trainer[2])
print(trainer[7])

print(std[-1])

'''
count a valid word from the scentance
1. word should be alpha numeric
2. it should have at least 1 vowel
3. it should have at least 1 consonant
4. it should have min 3 char


"I am a @utomation T3ster software 1234"

valid words are = T3ster,  software


aAABbBcCcDDdEeE--> aaABBBcccDddEEE

I am a @utomation T3ster software--> find second biggest word from the given string

Dillai devi
1. ie ili
2. vdili

'''

qua= "Santhosh"
print(qua+" Kumar")
qua.join("Kumar")
print(qua)

qua = qua+" Kumar"
print(qua)

print(qua[::-1])
# start : stop: step
print(qua[::3])

print(qua[1::2])
# count words
sen = "I am a @utomation T3ster software"
words = sen.split(" ")
print(words)

single = "Prathibha Arumugam"
print(single.split("a"))

alphanum = "abcd1efgh2ijkl3mnop4"
print(re.split("[0-9]", alphanum))
           # 0    1     2   3   4
std_mark = [450, 650, 250, 750, 950, 450, 650, 250, 450]

           # -5   -4   -3   -2   -1

print(len(std_mark))
print(len(alphanum))

print(std_mark[2])
print(std_mark[-2])

std_mark.append("Indhumathi")
print(std_mark)

print(std_mark.count(450))
print(std_mark.count(650))
std_mark.remove(450)
#std_mark.clear()

print(std_mark)

print(std_mark.extend(std_mark))
print(std_mark)
std_mark1 = [350, 550, 850, 1050, 150]
std_mark1.extend(std_mark)

print(std_mark1)


std_mark1.insert(2, "Guvi")
print(std_mark1)

std_mark1[3] = 10005
print(std_mark1)

#tuple

std_details = ("Ajith Kumar", "Vijay", "Suriya", "Trisha", "Vijay sethupathi", "Kalyani")

print(std_details)
print(std_details[-1])

#std_details[3] = "Aishwarya lakshmi"
print(std_details.index("Vijay"))

# Set
actress = {"Aishwarya lakshmi", "Madona", "Kalyani", "sreeleela", "Arthi", "trisha", "simran", "meena", "trisha", "simran", "meena"}

print(actress)

actress.add("Jothika")
actress.add("viola davis")
print(actress)
nineties_heroins = ("trisha","meena","ramba", "Jothika", "sneha", "simbran")
all = actress.difference(nineties_heroins)
print(all)

all_actress={"80's":{"Amala", "Revathi", "Rekha", "Ambika", "Radha"},
             "90's": {"trisha","meena","ramba", "Jothika", "sneha", "simbran"},
             "20's":["Aishwarya lakshmi", "Madona", "Kalyani", "sreeleela", "Arthi"]}

print(all_actress.values())
print(all_actress.keys())
print(all_actress.get("90's"))
print(all_actress.get("20's"))








