states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'Ney York'
cities['or'] = 'Oregon'

print '-'*10
print "Michigan abbreviation is", states['Michigan']
print "Michigan has state", cities[states['Michigan']]

for state, abbrev in states.items():
    print "%s is abbreviated as %s" %(state, abbrev)

state = states.get('texas')

if not state:
    print "wrong state"

city = cities.get('CA', 'CA')
print "The city for the state 'TX' is: %s" % city
