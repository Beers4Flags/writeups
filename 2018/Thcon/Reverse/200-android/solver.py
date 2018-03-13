#!/usr/bin/env python

from z3 import *
import os

solver = Solver()

# Define the serial characters
c0 = Int('c0')
c1 = Int('c1')
c2 = Int('c2')
c3 = Int('c3')
c4 = Int('c4')
c5 = Int('c5')
c6 = Int('c6')
c7 = Int('c7')
c8 = Int('c8')
c9 = Int('c9')
c10 = Int('c10')
c11 = Int('c11')
c12 = Int('c12')
c13 = Int('c13')
c14 = Int('c14')
c15 = Int('c15')
c16 = Int('c16')
c17 = Int('c17')
c18 = Int('c18')
c19 = Int('c19')

# Define the possible values for each characters,
# from ' ' and '~' (printable char).
solver.add((c0 >= 0x20, c0 <=0x7e))
solver.add((c1 >= 0x20, c1 <=0x7e))
solver.add((c2 >= 0x20, c2 <=0x7e))
solver.add((c3 >= 0x20, c3 <=0x7e))
solver.add((c4 >= 0x20, c4 <=0x7e))
solver.add((c5 >= 0x20, c5 <=0x7e))
solver.add((c6 >= 0x20, c6 <=0x7e))
solver.add((c7 >= 0x20, c7 <=0x7e))
solver.add((c8 >= 0x20, c8 <=0x7e))
solver.add((c9 >= 0x20, c9 <=0x7e))
solver.add((c10 >= 0x20, c10 <=0x7e))
solver.add((c11 >= 0x20, c11 <=0x7e))
solver.add((c12 >= 0x20, c12 <=0x7e))
solver.add((c13 >= 0x20, c13 <=0x7e))
solver.add((c14 >= 0x20, c14 <=0x7e))
solver.add((c15 >= 0x20, c15 <=0x7e))
solver.add((c16 >= 0x20, c16 <=0x7e))
solver.add((c17 >= 0x20, c17 <=0x7e))
solver.add((c18 >= 0x20, c18 <=0x7e))
solver.add((c19 >= 0x20, c19 <=0x7e))

# Define the constraints that have been
# founded in MainActivity.class.
solver.add(c4 == 45)
solver.add(c9 == 45)
solver.add(c14 == 45)
solver.add(c5 == (c6 + 1))
solver.add(c5 == c18)
solver.add(c1 == c18 % 4 * 22)
solver.add(c10 == c3 * c15 / c17 - 1)
solver.add(c10 == c1)
solver.add(c13 == c10 + 5)
solver.add(c10 == c5 - 9)
solver.add(c0 % c7 * c11 == 1440)
solver.add(c2 - c8 + c12 == c10 - 9)
solver.add((c3 + c12) / 2 == c16)
solver.add(c0 - c2 + c3 == c12 + 15)
solver.add(c3 == c13)
solver.add(c16 == c0)
solver.add(c7 + 1 == c2)
solver.add(c15 + 1 == c11)
solver.add(c11 + 3 == c17)
solver.add(c7 + 20 == c6)

# Check() returns true if there is a solution
# and model() the values of characters.
if solver.check():
	print(solver.model())
else:
	print('Not found.')
