file = "/Volumes/My Shared Files/shared/thispc_host/weekends/python_da_jan_26/python/tutorial_7_file/demo.csv"

# name = "Mahesh"
# age = 31
# tn = 89763
# tname = "Jalendhar Exp"
# from_city = "Pune"
# to_city = "Jaipur"
# distance = 550
# category = "3AC"
# date = "15/03/2026"

def writeInFile(name, age, tn, tname, from_city, to_city, distance, category, date):
    with open(file, "a") as fileobj:
        print("open success")
        
        fileobj.write(f"\n{name},{age},{tn},{tname},{from_city},{to_city},{distance},{category},{date}")
        
        
writeInFile("Mahesh",31,89763,"Jalendhar Exp","Pune","Jaipur",550,"3AC","15/03/2026")
writeInFile("Kamlesh",35,91763,"Malva Exp","Delhi","Ghaziabad",50,"SL","25/03/2026")

