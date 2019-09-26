'''import xlrd
loc = ("sample.xlsx")
wb =xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(sheet.nrows):
    print(sheet.cell_value(i, 0),  sheet.cell_value(i,1))
   # print(sheet.cell_value(i,1))'''


'''fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()'''

'''fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")
fo.close()
'''

'''fo = open("foo.txt", "r+")
str1 = fo.read(44)
print ("Read String is : ", str1)'''



'''import os
os.rename( "foo.txt", "test2.txt" )'''

import os
os.remove("test2.txt")


