my_text = "I love Monday mornings \n This might not be true for all"


def my_days(some_test):
    print("Welcome to Functions in Python")
    return some_test


my_days(my_text)


x = input("ENter name:")


def fnc(var):
    return var[::-1]


print(fnc(x))


number1 = 6
number2 = 15.3
divisor = 3.2


def some_operation(num1, num2, divd):
    global number1
    summ = number1 + 1
    division1 = number1 / divisor
    division2 = number2 / divisor
    # summ = division1 + division2
    return division1, division2, summ


print(f"this is number1 : {number1}")
div1, div2, sm = some_operation(number1, number2, divisor)
print("Division of the first number is ", div1)
print("Division of the first number is ", div2)
print("The sum of both numbers is ", sm)

width = 5
print(f"testing number1 {number1:<{width}d}")

# task12
from re import split
import sys


def getting_user_Data():
    
    N   = input("Enter your (Name): ")
    A   = input("Enter your (Age): ")
    AN  = input("Enter your (AccountNo(OLA X~X)): ")
    Adr = input("Enter your (Address): ") 
    Bal = input("Enter your (Balance): ")    
    if AN:
        return fnc(Name=N, Age=A, AccountNo=AN, Address=Adr, Balance=Bal)
    else:
        return fnc(Name=N, Age=A, Address=Adr, Balance=Bal)



def fnc(**args):
    args = {keys.lower(): value for keys, value in args.items()}
    if "accountno" in args:
        if (args["accountno"] != "") and ((args["accountno"])[:3] == "OLA"):
            if int(args["balance"]) >= 5:
                trans = input(
                    "What Transaction you would like to make?(Deposite/Withdraw/Loaning): "
                )
                return (
                    1  # it should return something here if the program is finished
                )
            else:
                print("Sorry we cant help you with any transction as ur balance below min requirments , better visit nearest branch to know more!")
                return 0
        else:
            print("Sorry your account number is not registered in our DB better visit our branch for more assistance!")
            return 2
    else :
        print("Sorry no account number was provided!")
        return 3


def main():
    feedback = getting_user_Data()
    if feedback != 1:
        sys.exit()
    else:
        print("Your program is working")
        pass  # thats if the program returned somthing beside True


main()
