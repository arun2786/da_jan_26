rows = int(input("Enter number of rows: "))

for row in range(rows):
    for col in range(rows//2):
        if col==0 or col == rows//2 - 1 or row ==0 or row == rows-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()