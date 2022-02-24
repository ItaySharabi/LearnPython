
print('\n------- import ___ as ___ -------\n')

import datetime

d1 = datetime.date(2000, 1, 1)
d2 = datetime.date(2010, 1, 31)

print(f'd1: {d1} \nd2: {d2} \n')

print('\n------- From ___ import ___ -------\n')
from datetime import date

d3 = date(2008, 5, 17)
d4 = date(1992, 2, 18)

print(f'd1: {d3} \nd2: {d4} \n')
