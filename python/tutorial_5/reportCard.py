# def printReport(name, roll, marks):
#     print(name)
#     print(roll)
#     print(marks)
    
    
# kwargs -> {'name': 'Ramesh', 'roll': 123}
def printReport(**kwargs):
    print(kwargs)
    
    
printReport(name="Ramesh",  roll=123, marks=61)
printReport(name="Ramesh",  roll=123, marks=61, phone="789886678")

