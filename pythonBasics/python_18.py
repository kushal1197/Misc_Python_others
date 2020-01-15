def print_two(*arg):                    #define a function
    arg1, arg2 , arg3 = arg             # define the arguments
    print "arg1: %r, arg2: %r, arg3: %r" %(arg1, arg2, arg3)    #define what to do with the input

def print_two_agaon(arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1, arg2)

def print_one(arg1):
    print "arg1: %r" %arg1

def print_none():
    print "i got nothing"

print_two("hello", "hi", "3")           #call the function. it will execute the steps define above
print_two_agaon("hello", "hi")
print_one("first")
print_none()
