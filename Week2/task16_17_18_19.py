# task 16:
s = "Software Development"

print(
    f"""{s[0],s[7],s[-3],len(s),s[16],
           s[5:8],s[-3:-6],s[-6:-3],s[:-3],s[5:],
           s[5:500],s[:],s[1:8:2],s[::2],s[::-1]}"""
)

# task 17:
print(f"s[0]: {s[0]} -> The first character of the string.")
print(f"s[7]: {s[7]} -> The eighth character of the string (index starts at 0).")
print(f"s[-3]: {s[-3]} -> The third-to-last character of the string.")
print(f"len(s): {len(s)} -> The total number of characters in the string.")
print(f"s[16]: {s[16]} -> The 17th character of the string (index 16).")

print(f"s[5:8]: {s[5:8]} -> Substring from index 5 to just before index 8.")
print(
    f"s[-3:-6]: {s[-3:-6]} -> An empty string because slicing from -3 to -6 with a default positive step is invalid."
)
print(
    f"s[-6:-3]: {s[-6:-3]} -> Substring from the 6th-to-last character to just before the 3rd-to-last character."
)
print(f"s[:-3]: {s[:-3]} -> All characters of the string except the last three.")
print(f"s[5:]: {s[5:]} -> Substring starting from index 5 to the end of the string.")

print(
    f"s[5:500]: {s[5:500]} -> Substring starting from index 5 to the end (no IndexError for out-of-range)."
)
print(f"s[:]: {s[:]} -> The entire string.")
print(f"s[1:8:2]: {s[1:8:2]} -> Characters from index 1 to 7, stepping by 2.")
print(f"s[::2]: {s[::2]} -> Every second character in the string.")
print(f"s[::-1]: {s[::-1]} -> The reverse of the string.")

# task 18
# (https://docs.python.org/3/library/stdtypes.html#str)

# task 19
print("\n\nTask 19:")
string = s[::-1].lower().capitalize()  # here it will reverse the string
string = string.replace(string[12:], string[:11:-1])
string = string.replace(string[16:], string[:15:-1])
string = string.replace(string[12:16], string[12:16].upper())
print(string)
