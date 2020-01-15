from sys import argv

script, user_name = argv
prompt = '>'
print "Hi %s, I am the %s script."%(user_name, script)
print "I would like to ask you few questions"
print "do you like me %s" %user_name
likes = raw_input(prompt)


print "where do you live %s?" %user_name
lives = raw_input(prompt)

print "what kind of computer you have?"
computer = raw_input(prompt)


print """
Alright, you have said %r about liking me.
you live in %r. not sure where is that.
and you have a %r computer. nice.
""" %(likes, lives, computer)
