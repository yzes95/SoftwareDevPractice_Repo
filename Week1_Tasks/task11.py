Cel = float(input("Enter the temp. in Fahrenheit: "))
#assuming the user will co-operate and enter a float

Fahr = ((9*Cel)/5)+32
Cel = ((Fahr-32)*5)/9

print(f"The temp. of {Cel} Celceius in Fahrenheit is : {Fahr} ")