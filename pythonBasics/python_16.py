from sys import argv

script, filename = argv

print "we are going to erase %r" %filename
print "if you don't want that press ctrl-c"
print "if you want that hit 'return'"

raw_input("?")                      #this displays "?" in a new line and wait for enter

print "opening %r" %filename
target = open(filename, 'w')        # 'w' option in the open function gives write permission
print "truncating the %r" %filename
target.truncate()                   # deleted the contents of file

print "now I am going to ask you for three lines"

line1 = raw_input("line 1 : ")
line2 = raw_input("line 2 : ")
line3 = raw_input("line 3 : ")

print "i am going to write these lines"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally we close it"
target.close()
print "these are the lines added to the %r" %filename
target = open(filename)
print target.read()
