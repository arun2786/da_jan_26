def createAccount(name,bal=2000):
    if (bal<2000):
        print("Not possible")
    else:
        print("Welcome",name,", your account is ready with bal:",bal)
    

createAccount("ramesh",5000)
createAccount("Mukesh",-100)
createAccount("Dinesh")
