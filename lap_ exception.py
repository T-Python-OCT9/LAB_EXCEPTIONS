

try:
    def additoin(x, y):
        x = 10
        y = 20
        print("Addition:", x + b)

        # NameError: name 'b' is not defined
    additoin(10, 20)

except NameError:
    print("the b is not defined ")
else:
    print("the operation is sucssful")
