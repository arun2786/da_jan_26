age = int(input("Enter your age: "))

# Valid for License age greater than 18 and less than 75


# if(age >= 18):
#     if(age<=75):
#         print("User can apply")
#     else:
#         print("Too senior")
# else:
#     print("Minor")

# if(age >= 18 and age<=75):
#     print("User can apply")
# else:
#     print("Minor or Too senior")
    
if(age < 18 or age>75):
    print("Minor or Too senior")
else:
    print("User can apply")
    
