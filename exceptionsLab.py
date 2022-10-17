
from tkinter.font import nametofont


def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + y)

   
try :
 additoin(10, 20)
except NameError:
   print ("b could not be found try another one..")  
else :
    ("the operation is successful")
