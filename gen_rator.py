
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(list(gen))


'''
Note: Notice the use of yield instead of return
each yeild pauses the funtion and remembers where it left off
'''

def read_file(filename):
    with open(filename) as f:
        for line in f:
            yield line

print(list(read_file("C://Users//sivan//PycharmProjects//Guvi_PythonSelenium//text_file.txt")))
for line in read_file("C://Users//sivan//PycharmProjects//Guvi_PythonSelenium//text_file.txt"):
    print(line)