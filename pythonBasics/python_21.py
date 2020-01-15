def add(a,b):
    print "adding %d + %d" %(a,b)
    return a+b                          #return gives a task to be defined in the function
    pass
def subtract(a,b):
    print "subtracting %d - %d" %(a,b)
    return a-b
    pass

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "lets do something with maths"

number_1 = int(raw_input())
number_2 = int(raw_input())
number_3 = int(raw_input())
number_4 = int(raw_input())
age = add(number_1,5)
height = subtract(number_2, 4)
weight = multiply(number_3, 2)
iq = divide(number_4, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, multiply(weight, subtract(height, add(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
