# Different ways to Import a library

# Method 1 - Standard Method
import calendar
print(calendar.calendar(2026))
print(calendar.month(2026,7))


# Method 2 - from and * (all)
from calendar import *
print(calendar(2026))
print(month(2026,7)) 


# Method 3 - from and specific , not all
from calendar import month
print(month(2026,7))
print(calendar(2026)) # error as only month from calendar is imported 

from calendar import calendar 
print(calendar(2026))
print(month(2026,7)) # error as only cal.. from calendar is imported 

# Therefore
from calendar import calendar , month # from Lib.. importing specific functions
print(calendar(2026))
print(month(2026,7))


# Method 4 - Variable from functions , libary name using as
import calendar as c
print(c.month(2026,7))

# Using as and from and import 
from calendar import month as m
print(m(2026,7))
