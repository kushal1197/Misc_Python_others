from sys import argv

#script, first, second, third = argv             # arguments will be required in the command line
#user_input_1 = raw_input("what is it?")
#user_input_2 = raw_input("what colour is it?")
#user_input_3 = raw_input("what shape is it?")
#user_input_4 = raw_input("what type is it?")
user_input_1, user_input_2, user_input_3, user_input_4 = argv
print "the script is called:", user_input_1           # this is the script to be run
print "the first variable is called:", user_input_2    # this is 1st argument the cmd line
print "the second variable is called:", user_input_3  # this is the 2nd argument the cmd line
print "the third variable is called:", user_input_4    # this  is the 3rd argument from the cmd line
