# task20
my_list = []
print(f"List Content: {my_list}")

# task21:
a = 1
b = 3.333333333
c1 = -9884
d1 = 3.552e04
c2 = a + b
d2 = [1, 3, 5, 7]
e = True
f = False
g = (1, 3, 5, 7)

my_list.append(a)
my_list.append(b)
my_list.append(c1)
my_list.append(c2)
my_list.append(d1)
my_list.append(d2)
my_list.append(e)
my_list.append(f)
my_list.append(g)

print(f"List Content: {my_list}")


# task22:
my_list.pop()  # here it will remove the last element added to the list
print(f"List Content: {my_list}")
my_list.remove(c2)  # remove 1st occurance of the value mentioned just the 1st
print(f"List Content: {my_list}")

# task23:
my_list.pop(3)  # remove element at index 3
print(f"List Content: {my_list}")

# task24
my_var = 0.05
my_list.insert(1, my_var)  # add an element at index 1
print(f"List Content: {my_list}")
my_list[2] = 0.06  # here replace an element
print(f"List Content: {my_list}")
