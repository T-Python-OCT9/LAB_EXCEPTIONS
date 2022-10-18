def additoin(x, y):
          x = 10
          y = 20
          print("Addition:", x + b)


try:
    additoin(10, 20)
except NameError:
    print("One of the variables is not defined ")
else:
    print("The operation is successful")