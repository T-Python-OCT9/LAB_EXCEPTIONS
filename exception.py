def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)
    raise NameError("This is a raised exception")


try:
    additoin(10, 20)
except NameError:
    print("Nameerror exception raised")
else:
    print("operation is successful")
finally:
    print("do some operation/s wether an exception is raised or not")
