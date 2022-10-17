def additoin(x, y):
    x = 10
    y = 20
    try:
        print("Addition:", x + b)
    except NameError as i:
        print(i.__class__)
        print("unindent does not match any outer indentation level")
        
    except:
        print("inter valid numbers")
    else:
        print("the operation is successful")


additoin(10,20)