from sys import argv

script, factor = argv
def test(factor_value):
    factor_value = int(factor_value)
    hydrogen = 10*factor_value
    oxygen = 11*factor_value
    return hydrogen, oxygen
    pass

#factor = int(raw_input("factor: ")
H, O2 = test(factor)
print """hydrogen has a molecule of %d velocity
Oxygen has a molecule of %d velocity""" %(H, O2)
