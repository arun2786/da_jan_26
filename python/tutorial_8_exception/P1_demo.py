try:
    name = None
    with open("./names.txt", "r") as fileobj:
        name = fileobj.read()

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(f"Nth char of name: {name[a]}")
    print(f"Divison: {a/b}")
except ZeroDivisionError:
    print("can not divide by zero")
except IndexError:
    print("name is smaller")
except FileNotFoundError:
    print("FileNotFoundError+++++++")
# except Exception as e:
#     print("unknown error")
# ZeroDivisionError
# IndexError
# FileNotFoundError