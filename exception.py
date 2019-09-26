'''try:
    #print(l[0])
    d = 10 / 0
except Exception as e:
    #print("You cannot devide by zero {0}".format(e))
    print("You cannot devide by zero {0}",e)
'''

'''l = []
try:
    print(l[0])
    
except IndexError as e:
    print(e)'''
'''l = []
try:
    print(l.get())

except AttributeError as e:
    print(e)'''

import math
def sqrt(x):
    if not isinstance(x,(int, float)):
        raise TypeError('x must be integer')
    elif x<0:
        raise ValueError("x cannot be negative")
    else:
        return math.sqrt(x)
try:
    print(sqrt("9"))

except Exception as e:
    print ("error",e)
try:
    print(sqrt(12))
except Exception as e:
    print ("error",e)