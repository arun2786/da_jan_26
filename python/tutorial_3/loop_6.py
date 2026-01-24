rows = 5

""" 
1 -> *
2 -> * *
3 -> * * * 
4 -> * * * * 
5 -> * * * * *
"""

# for row in range(1,rows+1):
#     for count in range(1,row+1):
#         print("* ",end="")
#     print()

for row in range(1,rows+1):
    print("* "*row)