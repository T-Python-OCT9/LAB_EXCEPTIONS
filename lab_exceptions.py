# Below you have a code that raises an exception , using what you learned do the following:
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

# Find what type of exception is raised.
# NameError


# Hanlde the exception in try..except
try:
    additoin(10, 20)
except NameError:
    # if operation fails, handle the specific exception that is raised , and print a relevant message.
    print("There's an error in one of the variables name.")
else:
    # If operation successful , print "the operation is successful"
    print("the operation is successful")
