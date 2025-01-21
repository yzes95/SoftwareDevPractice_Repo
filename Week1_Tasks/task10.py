import re
no1,no2= re.split(",| |/_",input("Enter 2 numbers  x & y respectively: "),flags = re.IGNORECASE)
#no exception is handled here
no1x = int(no1) 
no2y = int(no2) 
print("The Sum is        :",(no1x) + (no2y))
print("The Difference is :",(no1x) - (no2y))
print("The Product is    :",(no1x) * (no2y))
print("The Division is   :",(no1x) / (no2y))
