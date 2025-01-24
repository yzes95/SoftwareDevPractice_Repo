#task 3
Boolean_var_T = True
Boolean_var_F = False

print(
    f""" 
      For int :
      The Integer Value for the True value  = {int(Boolean_var_T)}
      The Integer Value for the False value = {int(Boolean_var_F)}

      For float :
      The Float Value for the True value  = {float(Boolean_var_T)}
      The Float Value for the False value = {float(Boolean_var_F)}

      For str :
      The String Value for the True value  = {str(Boolean_var_T)}
      The String Value for the False value = {str(Boolean_var_F)}
      """
)


#task 4
#it is same as before but we will just try testing the list one :

try:
  print(
    f""" 
      For list :
      The List Value for the True value  = {list(Boolean_var_T)}
      The List Value for the False value = {list(Boolean_var_F)}
      """
  )
except TypeError:
  print("!!!The Testing Case for list didnt print cause the boolean var \n is not of an iterable thing to iterate over!!!\n\n")

#task 5:
var = input("Enter a number to test cases on it: ")
if var.isnumeric():
  var_i = int(var)
  var_f = float(var)
  var_s = str(var)
  print(
      f""" 
        For int :
        The Integer Value ({var_i}) represented in bool as  = {bool(var_i)}
        The Integer Value ({var_i}) represented in bool as  = {bool(var_i)}

        For float 
        The Float   Value ({var_f}) represented in bool as  = {bool(var_f)}
        The Float   Value ({var_f}) represented in bool as  = {bool(var_f)}

        For str :
        The String  Value ({var_s}) represented in bool as  = {bool(var_s)}
        The String  Value ({var_s}) represented in bool as  = {bool(var_s)}
        """
  )
else:
  print("Data Entered wasnt a whole number!!!")


#task 6:
a = 1; b = 3.333333333
c = -9884; d = 3.552E+04
c = a + b; d = [1,3,5,7]
e = True; f = False
g = (1,3,5,7)

try:
  print(f"The Value of a is = {a:7} , as float   = {float(a)} and as string = {str(a)}")
  print(f"The Value of b is = {b:5.5f} , as integer = {int(b)}   and as string = {str(b)}")
  print(f"The Value of c is = {c:5.5f} , as integer = {int(c)}   and as string = {str(c)}")
  print(f"The Value of e is = {e:5.5f} , as float   = {float(a)} and as list   = {list(a)}")
except TypeError:
  print("!!!The Testing Case for (e) didnt print cause the boolean var \n is not of an iterable thing to iterate over!!!\n\n")
