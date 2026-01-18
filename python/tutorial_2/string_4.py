"""
email
    ramesh@gmail.com
    rajesh@gmail
    @ram@gmail.com
    nit...esh@gmail.com
    nitesh@gmail@com
    java.arun@kumar_gmail.com
    
    find if given email id is valid or not
    
    count, index, 
"""

"""
first.last@gmail.com
first_last@gmail.com

"""
import re

email = "ramesh_123.kumar@gmail.com"
# pattern = "^[a-z0-9A-Z]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"
pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


if re.match(pattern, email):
    print("valid")
else:
    print("invalid")