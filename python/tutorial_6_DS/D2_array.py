import array

# array vs list

def doTask():
    pass 

data = ["Ramesh", 32, False, doTask]

print(f"type: {type(data)}")


nums = array.array('i', [1, 2, 3, 4, 5])
print(f"type: {type(nums)}")

# --------------

# def sendNotification(std):
#     email = std.email
#     print("Sending notification to",email)
    
# stdList = [ram, shyam, "mohan", 54]

# for std in stdList:
#     sendNotification(std)