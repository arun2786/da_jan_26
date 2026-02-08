# file = "/Volumes/My Shared Files/shared/thispc_host/weekends/python_da_jan_26/python/tutorial_7_file/demo.csv"
# file = "./python/tutorial_7_file/demo.csv"
file="./abc.csv"

with open(file, "a") as fileobj:
    print("open success")
    fileobj.write("\nthis is a python tutorial.")