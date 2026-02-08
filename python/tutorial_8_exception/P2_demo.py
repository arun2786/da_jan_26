name = None
with open("./names.txt", "r") as fileobj:
    name = fileobj.read()

try:
    a = int(input("Enter first number: "))
except ValueError:
    print("invalid input")

b = int(input("Enter second number: "))

print(f"Nth char of name: {name[a]}")
print(f"Divison: {a/b}")