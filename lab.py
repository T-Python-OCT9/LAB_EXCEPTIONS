def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError: # if operation fails, handle the specific exception
    print("Name 'b' Is Not Defined!")
else: # If operation successful
    print("The Operation Is Successful")
