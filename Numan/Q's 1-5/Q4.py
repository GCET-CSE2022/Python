"""
Author: Numan
Dated: 11-04-2025

"""
# 4. Write a python script to print the current date in the following format "Sub May 29 02:26:23 IST 2017".

import time;
currTime=time.localtime()
print(currTime)
# strf()----> built in fxn in time module that formats time values into the strings.
finalTime=time.strftime("%a %b %d %H:%M:%S IST %Y", currTime)
print(finalTime)

"""
Key points:

a --> weeday
b --> month
d --> day of the month
H --> hour(24-hour format)
M --> minutes
S --> seconds
Y --> year
IST--> Indian Standard Time(HArd coded)
 
"""