print("Hello")

li = [1, 3, 5]
tp = (9, 4, 5, 8)

li.append(tp)
print(li)

a = []
b = set(a)
b.add(9403)


'''
Type casting--> converting one data type  into another
like int --> String
flot --> string
string --> int

'''
z = 10
print(type(z))

x = str(z)
print(type(x))
print(z+44)
print(x+"99")

dic = {"sivanesh":999, 'Santhosh': 1020}
print(type(dic.keys()))
print(dic.keys())
print(dic.values())
value = list(dic.values())
print(value)

dic2 = {"Indhu":1200, "pradhiba": 1100}

dic.update(dic2)
print(dic)
dic.pop("sivanesh")
print(dic)

d = 897

e = d % 10
print(e)

f = d//10
print(f)

d = f
print(d)


