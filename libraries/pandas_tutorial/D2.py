import pandas as pd

# names = ["Ramesh", "Suresh","Dinesh","Mukesh"]
# ages = [29, 31,27,28]
# marks = [79, 81,77,82]

# DataFrame - think as excel table
students_1 = pd.DataFrame({
    "names" : ["Ramesh", "Suresh","Dinesh","Mukesh"],
    "ages" : [29, 31,27,28],
    "marks" : [79, 81,77,82]
})

print(students_1)

print("\n=============\n")
students_2 = [
    ["Ramesh",29,79],
    ["Suresh",31,81],
    ["Dinesh",27,77]
]
std = pd.DataFrame(students_2, columns=['Name','Age','Score'])

print(std)