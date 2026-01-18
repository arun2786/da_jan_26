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

email = "ramesh_.gm4ail_com@@gmail.com"

# 1. must contain @
# 2. must contain .
# 3. @ should not be first char
# 4. . should not be first char
# 5. @ should not be duplicate
# 6. @ should not be last char
# 7. . should not be last char

if '@' not in email:
    print("checking @ availability")
    print("Email does not contain '@' character.")
elif '.' not in email:
    print("checking . availability")
    print("Email does not contain '.' character.")
# if email[0]=='@':
elif email.startswith('@'):
    print("Email can not start '@' character.")
# if email[-1]=='@':
#     print("Email can not start '@' character.")
# must end with @gmail.com
# if email[-10:]!='@gmail.com':
elif not email.endswith('@gmail.com'):
    print("Email must end '@gmail.com'.")


else:
    # email must contain at least 8 chars
    
    if(len(email)<8):
        print("Invalid lenght")
    else:
        print("Valid email")