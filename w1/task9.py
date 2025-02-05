import re
x,y,z= re.split(",| |/_",input("Enter three numbers to be added: "),flags = re.IGNORECASE)
print("The sum is :",(int(x)+int(y)+int(z)))
#Much more can be done using regular expressions 
#Req to be revised later
# The + sign can be used to add 2 of same type but not diff u cant add a string + int