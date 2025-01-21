from random import random

for i in range(-1,6,1):
    print(i+1,end = " ")
    for j in range(1,7,1):
        if(i == -1):
            print(f"{j:7}",end =" ")
        else:
            print(f"{random():0.5f}",end = " ")
    print()        

