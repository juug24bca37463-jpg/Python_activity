
Aim

To study and implement basic functions of Python’s `re` module for pattern matching and string operration

 Algorithm

1. Start the program
2. Import the `re` module
3. Define a sample string
4. Use `match()` to check pattern at the beginning
5. Use `search()` to find a pattern in the string
6. Use `findall()` to get all matches
7. Use `finditer()` to display matches with position
8. Use `sub()` to replace characters
9. Use `split()` to split the string
10. Use `compile()` to create a reusable pattern
11. Take date input and validate using `fullmatch()`
12. Stop the program

CODE:
import re
text = "My email is shivani@gmail.com and phone is 9123456789"

# 1. re.match() - Checks for a match only at the beginning of the string
pattern_match = r"My"
match_result = re.match(pattern_match, text)
if match_result:
    print("1. match():", match_result.group())
else:
    print("No match")

# 2. re.search() - Searches the entire string for a match
pattern_search = r"\d{10}"
search_result = re.search(pattern_search, text)
if search_result:
    print("2. search():", search_result.group())
else:
    print("Not found")

# 3. re.findall() - Returns a list of all matches
pattern_findall = r"\w+@\w+\.\w+"
findall_result = re.findall(pattern_findall, text)
print("3. findall():", findall_result)

# 4. re.finditer() - Returns an iterator yielding match objects
print("4. finditer():")
for match in re.finditer(pattern_findall, text):
    print("Found:", match.group(), "at position", match.start())

# 5. re.sub() - Replaces matches with a replacement string (digits to *)
pattern_sub = r"\d"
sub_result = re.sub(pattern_sub, "*", text)
print("5. sub():", sub_result)

# 6. re.split() - Splits the string by whitespace
pattern_split = r"\s"
split_result = re.split(pattern_split, text)
print("6. split():", split_result)

# 7. re.compile() - Compiles a pattern for reuse
pattern_compile = re.compile(r"\w+")
compiled_result = pattern_compile.findall(text)
print("7. compiled pattern:", compiled_result)

# Date Validation using re.fullmatch()
date = input("Enter date (DD/MM/YYYY): ")
pattern = r"^\d{2}/\d{2}/\d{4}$"

if re.fullmatch(pattern, date):
    print("Valid date format")
else:
    print("Invalid date format")

 Output:
  1. match(): My
2. search(): 9123456789
3. findall(): ['shivani@gmail.com']
4. finditer():
Found: shivani@gmail.com at position 12
5. sub(): My email is shivani@gmail.com and phone is **********
6. split(): ['My', 'email', 'is', 'shivani@gmail.com', 'and', 'phone', 'is', '9123456789']
7. compiled pattern: ['My', 'email', 'is', 'shivani', 'gmail', 'com', 'and', 'phone', 'is', '9123456789']

Enter date (DD/MM/YYYY): 20/02/2026
Valid date format

Enter date (DD/MM/YYYY): 33/01/203
Invalid date format
