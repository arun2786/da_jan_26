num = int(input("Enter a number: "))

# find fizzbuzz
if(num % 3 == 0 and num % 5 == 0):
    print("FizzBuzz")
# find fizz
elif (num % 3 == 0):
    print("Fizz")
# find buzz
elif(num % 5 == 0):
    print("Buzz")
else:
    print("Nothing")