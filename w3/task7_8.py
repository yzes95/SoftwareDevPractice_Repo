#question 7

# Define the number of rows for the triangle
num_rows = 5
# Outer loop for each row
for i in range(1, num_rows + 1):
# Inner loop to print stars in each row
    for j in range(i):
        print("*", end="")
    # Move to the next line after each row
    print()


#question 8 using while:
num_rows = 1
while num_rows <= 5:
    print("*"*num_rows)
    num_rows+=1
    
