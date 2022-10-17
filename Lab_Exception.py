def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


#Find what type of exception is raised. ->>>> NameError
try:
    additoin(10, 20)
#if operation fails, handle the specific exception that is raised , and print a relevant message.
except NameError:
    print("Name 'b' is not defined")
else:
    print("The operation is successful")



