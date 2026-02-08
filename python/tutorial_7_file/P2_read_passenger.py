# filepath = "/Volumes/My Shared Files/shared/thispc_host/weekends/python_da_jan_26/python/tutorial_7_file/passengers.csv"
filepath = "/Volumes/My Shared Files/shared/thispc_host/weekends/python_da_jan_26/python/tutorial_7_file/demo.csv"

with open(filepath) as fileobj:
    # print(fileobj.read())
    # print(fileobj.readlines())
    lines = fileobj.readlines()
    print("----- Passenger Detail -------")
    for i in range (len(lines)):
        if(i!=0):
            # print(lines[i])
            passenger_list = lines[i].split(",")
            name = passenger_list[0]
            age = passenger_list[1]
            train_num = passenger_list[2]
            train_name = passenger_list[3]
            print(f"Name:\t\t{name}")
            print(f"Age:\t\t{age}")
            print(f"Train:\t\t{train_num}")
        print("==================",end="\n")
