from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" %(from_file, to_file)

#infile = open(from_file)                           #open the source file
#indata = infile.read()                             # read the data from source file
indata = open(from_file).read()                     #shorter way of doing above 2 lines
print "the input file is of %d bytes long" %len(indata) #read in the length of source data

print "does the output file exists? %r" %exists(to_file) #condition for existance of target file

print "ready? hit return to continue or press ctrl+c"
raw_input()

#out_file = open(to_file, 'w')                       # open target file in write mode
#out_file.write(indata)                              # write source data in target file
out_file = open(to_file, 'w').write(indata)
print "all done"

#out_file.close()                                      #is not needed when write is issued in same line as open 
#infile.close()
