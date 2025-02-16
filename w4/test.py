from datetime import datetime
from re import split

def main():
    time_discount = 10/100
    y,m,d = map(int,split(" |,|:|-|/",input("Enter the Date (YY/MM/DD): ")))
    H,M,S = split(":",datetime(year = y,month = m, day = 7).now().time().strftime("%H:%M:%S"))
    Age = int(input("Enter Your Age: "))
    bill = float(input("Enter your recipt value: "))
    age_d = Age_checker(Age)
    if int(H) > 17:
        bill -= (bill*(age_d+time_discount))
    else:
        bill -= (bill*(age_d))
    print(f"Your Bill is : {bill}")
    

def Age_checker(age:int)->float:
    u_18 = 20/100
    o_70 = 30/100
    if age < 18:
        return u_18
    elif age >= 70 :
        return o_70
    else:
        return 0
# here will be the fnctions to be called
#checktage(age)
#print(HR,MIN,SEC)

if __name__ == "__main__":
    main()

    

