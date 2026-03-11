AIM

To implement basic string operations in Python such as reversing a string, finding length, checking palindrome, converting case, counting vowels and verifying substring presence.

Algorithm

Start the program.
Assign a string to a variable.
Display the reverse of the string using slicing.
Find the total number of characters using the length function.
Compare the string with its reverse to check palindrome.
Convert the string to uppercase and lowercase forms.
Use a loop to count vowels in the string.
Check whether a given substring is present.
Print all results and terminate the program.

SOURCE CODE

s = "HELLOWORLD"
print(s[:: -1])
count = len(s)
print(count)
if s == s[:: -1]:
     print("Palindrome")
else:
    print("Not a Palindrome")
print(s.upper())
print(s.lower())
vowels = "aeiouAEIOU"
count = 0
for ch in s:
     if ch in vowels:
          count += 1
print("Number of vowels:",count)

sub = "WORLD"
if s.count(sub)>0:
       print("Substring exists")
else:
    print("Substring does not exist")

n = int(input("Enter a number:"))
fact = 1
i = 1
while i<n:
     fact = fact * i
     i += 1
     print(fact)

Output:
DLROWOLLEH
10
Not a Palindrome
HELLOWORLD
helloworld
Number of vowels: 3
Substring exists 
Enter a number : 5
1
2
6
24
120
