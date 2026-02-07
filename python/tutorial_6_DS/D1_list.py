# name = "aman"
# name.append("kumar")

# stds = [] # List 
stds = ["Ramesh", "Suresh", "ashwani"] # List 

print(f"Type: {type(stds)}")
print(f"Value: {stds}")


print(f"First value: {stds[0]}")
print(f"Last value: {stds[-1]}") # only python gives
lastIndex = len(stds)-1
print(f"Last value: {stds[lastIndex]}")
print(f"Last value: {stds[-1:]}") # only python gives

print(f"First two: {stds[0:2]}")


# CRUD

# Create - add
stds.append("Mahesh") # insert at last
stds.append("Dinesh")

# Update - modify
stds[2] = "ashwini"

# Delete 
# stds.remove("Ganesh") # error
stds.remove("ashwini") # error

# Read all values
for i in range(len(stds)):
    print(f"{i+1} -> {stds[i]}")

# print("[", end="")
# for i in range(len(stds)):
#     print(f"{stds[i]}, ", end="")
# print("]")

# for std in stds:
#     print(std)