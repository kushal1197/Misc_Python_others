#import argument module
from sys import argv

#define number of arguments to be given in the command line
script, filename = argv
#open the file given in the command line argument
txt = open(filename)

print "here is your file %r:" %filename
print txt.read()                        # read the file content
txt.close()                             # it is important to close a file

#another way of doing it is raw_input
print "type the file name again"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
