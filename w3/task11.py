#question11
for count1 in range(1,10):
    for count2 in range(1,5):
        multiplication = count1*count2
    if multiplication%3 != 0:
        division = multiplication/3
        print("""The {} x {} is not divisible by 3. The result is 
              {:.6f}""".format(count1,count2,division))
        
#the .6f determine that the max decimal places to be printed are 6
