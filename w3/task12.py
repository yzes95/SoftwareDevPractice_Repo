"""
You are tasked with creating a program that demonstrates the formatting and alignment of integers, but with the following constraints:

Dynamic Width: The program should be able to handle output widths up to 100 characters.
Variable Number of Integers: The program should be able to format and align an arbitrary number of integers provided by the user, with no predefined limit.
Error Handling:
The program should gracefully handle invalid input, such as:
Non-numeric values in the integer input.
Invalid alignment options (e.g., "left", "right", "center", and any other input should be considered invalid).
Output widths outside the acceptable range (e.g., negative width, width greater than 100).
The program should provide informative error messages to the user.
Efficiency: The program should be implemented efficiently, considering the potential for large inputs (many integers and wide output widths) and the need for fast processing.
File Handling: The program should be able to read input integers from a file and write the formatted output to another file.
Specific Requirements:

Input:
The program should first prompt the user for the desired output width.
The program should then prompt the user to choose between:
Manual Input: Enter integers directly from the console, separated by spaces.
File Input: Read integers from a specified input file.
Finally, it should prompt the user for the desired alignment: "left", "right", or "center".
Output:
The program should display the formatted integers according to the user's specifications.
The output should be neatly presented with clear labels for each alignment.
Error messages should be informative and guide the user on how to correct the input.
If file input is chosen, the formatted output should be written to a specified output file.
Example Output (Partial, for illustration):

Enter desired output width: 20 
Choose input method (manual/file): manual
Enter integers: 123 45 6789 10 
Enter alignment (left, right, center): center

Left-aligned:       123
Right-aligned:      123     
Center-aligned:    123     

... (Output for remaining integers)

This problem:

Increases the complexity of input handling.
Introduces file I/O operations.
Enforces stricter input validation.
Places a greater emphasis on program robustness and efficiency.
This significantly increases the challenge, requiring a more robust and well-structured solution.
"""
from re import split
import sys
def left_align(width,numbers):
    for number in numbers:
        print(f"{int(number):<{width}d}")

def main():
    try:
        d_width=int(input("Enter desired output width:"))
        method=input("Enter the desired method(manual/file):").lower()
        numbers=split(' |_|,|-',input("Enter the integers required:"))
        alignment=input("Enter Alignment (left, right, center):").lower()
        match method:
            case "manual" | "file":
                pass
            case _:
                sys.exit("wrong data aquestion method!!!")

        for number in numbers:
            if number.isnumeric:
                pass
            else:
                raise ValueError

        match alignment:
            case "left":
                left_align(d_width,numbers)
            case "right":
                pass
            case "center":
                pass
            case _:
                sys.exit("Wrong Alignment have been entered!!!")
    except Exception as e:  
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Message: {e}")


if __name__ == "__main__":
    main()
    
