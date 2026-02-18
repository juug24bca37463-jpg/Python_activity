S = "HELLOWORLD"
print(S[::-1])

S = "HELLOWORLD"
count = len(S)
print(count)

S = "HELLOWORLD"
if S == S[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

S = "HELLOWORLD"
print(S.upper())
print(S.lower())

S = "HELLOWORLD"
sub = "WORLD"
if S.count(sub) > 0:
    print("Substring exists")
else:
    print("Substring does not exist")

S = "HELLOWORLD"
vowels = "aeiouAEIOU"
count = 0
for ch in S:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)

n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    print(fact)
    i += 1

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
  
