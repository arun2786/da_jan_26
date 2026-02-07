# List -> []
# Tuple -> () or nothing

def findStudent(roll):
    # read database or read file
    name = "Ramesh"
    age = 19
    cgpa = 8.7
    
    # return name, age, cgpa, roll
    return (name, age, cgpa, roll)


std = findStudent(123)
# std[2] = 99.9
print(f"Name: {std[0]}")
print(f"Roll: {std[3]}")
print(f"Age: {std[1]}")
print(f"Score: {std[2]}")
