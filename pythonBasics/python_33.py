def create_list(x, y):
    i = 0
    numbers = []
    while i < x:
        print "At the top i is %d" % i
        numbers.append(i)

        for i in range(i, y+1):
            print "Numbers now: ", numbers
            print "At the bottom i is %d" % i


        print "The numbers: "

        for num in numbers:
            print num

# used below commands in another file to call the above function
#test_number = int(raw_input("> "))
#incremental = int(raw_input("> "))

#create_list(test_number, incremental)
