from math import sqrt
from re import split

print(
    """
      -b +- sqrt(b^2 - 4ac)
x = -------------------------
               2a
      """
)
a, b, c = map(
    float,
    split(
        ",|_| |-",
        input(
            "Enter the values for the variables (a,b,c) respectively to get the value of x: "
        ),
    ),
)

try:
    x1 = complex((-b + sqrt((b * b) - (4 * a * c))) / (2 * a))
    x2 = complex((-b - sqrt((b * b) - (4 * a * c))) / (2 * a))
except ValueError:
    x1 = complex(-b / (2 * a), ((b * b) - (4 * a * c)) / (2 * a))
    x2 = complex(-b / (2 * a), -(((b * b) - (4 * a * c)) / (2 * a)))

print(
    f"""The value of x will be either : 
       {x1}
       {x2}"""
)
