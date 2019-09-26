'''l=[4,6,1,0,3]
print("before shorting list is{0}".format(l))
l.sort()
print("after shorting{0}".format(l))'''

'''def getdiffreance(a,b):
    if isinstance(a,int):#it checkes the data type of a if it matches then it will return true or else false
        return a-b;
print("hi")
a=5;
b=5.5;
c=getdiffreance(a,b)
print(c)'''


def getvalues(a, pi=3.141, c=None):
    print(pi)
    input("hold")
    if c is not None:
        print(c)
        return a + pi + c
    return a + pi


print("hii")
if __name__ == '__main__':
    print(getvalues(4,10,20))
    #print(getvalues(4,10))


