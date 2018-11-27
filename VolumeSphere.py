#
from math import pi
#
in_file = open('input_diameter.txt')
#
d = input("write diameter number: ")
r = float(d)/2
V = (4/3)*pi*(r**3)
print("Volume of sphere:%s " %V)
