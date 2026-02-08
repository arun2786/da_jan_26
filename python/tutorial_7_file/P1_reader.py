filepath = "/Volumes/My Shared Files/shared/thispc_host/weekends/python_da_jan_26/python/tutorial_6_DS/hw.txt"

# fileobj = open(filepath)
# # code
# fileobj.close()

with open(filepath) as fileobj:
    print(fileobj.read())