#Find what type of exception is raised.
# the type of exception is "NameError"

def additoin(x, y):
          x = 10
          y = 20
          print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError:
    print("please checkk the name of var")
else:
    print("The operation is successful")
finally:
    print("Exceuted no matter the operation is done or not")


