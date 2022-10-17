
   
def additoin(x, y):
    x = 10
    y = 20

    print("Addition:", x + b)
   
try:
    additoin(2,4)
except NameError:
     print("operation fails")  

except Exception as e:
     print("Type the exception is: ",e.__class__)
            
else:
    print("the operation is successful") 
             


additoin(10, 20)