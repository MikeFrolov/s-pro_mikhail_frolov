string = input("Enter the text:")

uppercase = 0
lower_case = 0

for ch in string:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lower_case += 1

if uppercase > lower_case:
    print(string.upper())
else:
    print(string.lower())

