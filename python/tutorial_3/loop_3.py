# print table of a number

num = 4

count = 1
while count<11:
    if count == 5:
        count = count + 1
        continue
    if count == 8:
        break
    print(f"{num} * {count} = {num * count}")
    count = count + 1
