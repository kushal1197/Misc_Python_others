from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
    pass

def rewind(f):
    f.seek(0)
    pass

def print_a_line(line_count, f):
    print line_count, f.readline()
    pass

current_file = open(input_file)

print "let's print the whole file:\n"
print_all(current_file)

print "now lets rewind the file"
rewind(current_file)

print "lets print input line and 3 more jumps:"
#current_line = int(raw_input("which line do you want?: "))
#jump = int(raw_input("what is the jump value?: "))

current_line = 1

print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
