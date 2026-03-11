AIM

To study and implement different operators in Python and verify algebraic identities, bitwise relationships, and arithmetic operations like addition and subtraction.

Algorithm
Begin the program.
Create two integer variables where a is equal to 208 and b is equal to 600.
Display a heading indicating that equation identities will be checked.
Use Python expressions to test several algebraic formulas and print whether they are true or false.
After that print a heading to show the start of bitwise operator verification.
Apply bitwise operators such as AND, OR and XOR and check the relationship between them.
Next display the heading for addition.
Verify addition using bitwise operator relations and print the results.
Then display the heading for subtraction.
Use different bitwise expressions to confirm subtraction results.
Print all the evaluated results on the screen.
Terminate the program.

SOURCE CODE

a = 208
b = 600

print("In equation Assignment operators:\n")

print((a+b)**2 == (a**2 + 2*a*b + b**2))
print((a-b)**2 == (a**2 - 2*a*b + b**2))
print((a+b)*(a+b) == 2*(a**2 - b**2))
print((a+b)+(a-b) == 2*a)
print((a**3 + b**3) == (a+b)*(a**2 - a*b + b**2))

print("In Bitwise operators")

print((a | b) == ((a ^ b) + (a & b)))
print((a ^ (a & b)) == ((a | b) ^ b))
print((b ^ (a & b)) == ((a | b) ^ a))
print(((a & b) ^ (a | b)) == (a ^ b))

print("In Addition\n")

print((a + b) == ((a | b) + (a & b)))
print((a + b) == ((a ^ b) + 2*(a & b)))

print("In Subtraction\n")

print((a - b) == ((a ^ (a & b)) - ((a | b) ^ a)))
print((a - b) == (((a | b) ^ b) - (b ^ (a & b))))
print((a - b) == ((a ^ (a & b)) - (b ^ (a & b))))
print((a - b) == (((a | b) ^ b) - ((a | b) ^ a)))

OUTPUT :

In equation Assignment operators:

True
True
False
True
True

In Bitwise operators
True
True
True
True

In Addition

True
True

In Subtraction

True
True
True
True
