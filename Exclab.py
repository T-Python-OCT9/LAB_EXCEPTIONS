

def additoin(x, y):
          x = 10
          y = 20
          print("Addition:", x + b)
        


try:
    additoin(10, 20)
except NameError:
    print("some variable doesn't exist")
else:
    print("the operation is successful")
finally:
    print("Variable b in not defined")
