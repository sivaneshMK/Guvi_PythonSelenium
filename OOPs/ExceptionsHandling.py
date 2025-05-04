def div(numerator, denominator):
    name = "abcd"
    try:
        print(int(name))
        print(numerator/denominator)
    except ZeroDivisionError:
       print("denominator is zero")
    except ValueError:
        print("Value Error")
    finally:
        print("print Finally")


div(1, 3)
div(3,3)
div(1, 0)

print("wiv")

age = 4
if age>= 18:
    print("your eligible to vote")
else:
    raise ValueError("your not eligible to vote")



