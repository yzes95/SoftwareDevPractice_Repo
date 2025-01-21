import re
from math import sqrt

a,b,c= re.split(",| |/_",input("Enter the length of the three sides of the triangle: "))

A = int(a)
B = int(b)
C = int(c)

S = 0.5*(A+B+C)

Area = sqrt((S*(S-A)*(S-B)*(S-C)))

print(f"The Area of the triangle is : {Area:0.6f}")