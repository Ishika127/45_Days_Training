# ==========================================
# STRING IN PYTHON - SLICING AND FUNCTIONS
# ==========================================

# Creating a string
text = "Hello Python World"

print("Original String:", text)

# ==========================================
# STRING SLICING
# ==========================================

# Get characters from index 0 to 4
print("text[0:5] =", text[0:5])

# Get characters from beginning to index 4
print("text[:5] =", text[:5])

# Get characters from index 6 to end
print("text[6:] =", text[6:])

# Get last character
print("text[-1] =", text[-1])

# Get last 5 characters
print("text[-5:] =", text[-5:])

# Reverse the string
print("text[::-1] =", text[::-1])

# Skip every second character
print("text[::2] =", text[::2])

# ==========================================
# STRING LENGTH
# ==========================================

# Find length of string
print("Length =", len(text))

# ==========================================
# CONVERT CASE
# ==========================================

# Convert to uppercase
print("Uppercase =", text.upper())

# Convert to lowercase
print("Lowercase =", text.lower())

# Convert first letter of string to uppercase
print("Capitalize =", text.capitalize())

# Convert first letter of every word to uppercase
print("Title =", text.title())

# Swap uppercase to lowercase and vice versa
print("Swapcase =", text.swapcase())

# ==========================================
# SEARCHING FUNCTIONS
# ==========================================

# Find position of substring
print("Find 'Python' =", text.find("Python"))

# Find position of substring (raises error if not found)
print("Index of 'World' =", text.index("World"))

# Check if substring exists
print("'Python' in text =", "Python" in text)

# ==========================================
# REPLACE FUNCTION
# ==========================================

# Replace a word
print("Replace =", text.replace("Python", "Java"))

# ==========================================
# COUNT FUNCTION
# ==========================================

# Count occurrences
print("Count of 'o' =", text.count("o"))

# ==========================================
# STARTS WITH / ENDS WITH
# ==========================================

# Check starting word
print("Starts with Hello =", text.startswith("Hello"))

# Check ending word
print("Ends with World =", text.endswith("World"))

# ==========================================
# SPLIT FUNCTION
# ==========================================

# Split string into list
words = text.split()
print("Split =", words)

# ==========================================
# JOIN FUNCTION
# ==========================================

# Join list elements into string
joined = "-".join(words)
print("Join =", joined)

# ==========================================
# REMOVE SPACES
# ==========================================

str1 = "   Python Programming   "

# Remove spaces from both sides
print("Strip =", str1.strip())

# Remove spaces from left side
print("Lstrip =", str1.lstrip())

# Remove spaces from right side
print("Rstrip =", str1.rstrip())

# ==========================================
# CHECKING FUNCTIONS
# ==========================================

s1 = "Python123"
s2 = "12345"
s3 = "PYTHON"
s4 = "python"

# Check if all characters are letters
print("isalpha =", s1.isalpha())

# Check if all characters are digits
print("isdigit =", s2.isdigit())

# Check if all characters are alphanumeric
print("isalnum =", s1.isalnum())

# Check if all letters are uppercase
print("isupper =", s3.isupper())

# Check if all letters are lowercase
print("islower =", s4.islower())

# Check if first letter of each word is capital
print("istitle =", "Hello World".istitle())

# ==========================================
# STRING CENTER, LEFT AND RIGHT JUSTIFY
# ==========================================

print("Center =", "Python".center(20, '*'))
print("Ljust =", "Python".ljust(20, '-'))
print("Rjust =", "Python".rjust(20, '-'))

# ==========================================
# STRING FORMAT
# ==========================================

name = "Ishika"
age = 19

print("My name is {} and I am {} years old.".format(name, age))

# Using f-string
print(f"My name is {name} and I am {age} years old.")

# ==========================================
# STRING COMPARISON
# ==========================================

a = "Apple"
b = "Banana"

print("a == b :", a == b)
print("a < b :", a < b)

# ==========================================
# ESCAPE CHARACTERS
# ==========================================

print("Hello\nWorld")   # New line
print("Hello\tWorld")   # Tab space
print("He said \"Python\"")  # Double quotes

# ==========================================
# END OF STRING PROGRAM
# ==========================================