""" 
    Update names in array for drafting email
"""

import openpyxl
from tkinter import *

# address book
book = openpyxl.load_workbook(r'./Address_book.xlsx')
ws = book.active


# array for names
nameArray = []

#APPEND NAMES IN LIST, RUNNING THROUGH COLUMN A OF THE SHEET UNTIL THERE'S AN EMPTY CELL
skip=True
firstRow=True
for cell in ws['A']: 
    if (cell.value==None):  
        continue 
    if (skip==False):  
        nameArray.append(cell.value) 
        firstRow=False 
    skip=False

#PRINT ALL ITEMS IN THAT ROW TO SEE THAT IT WORKS
for x in nameArray:
    print(x)

#DISPLAY SUCCESS MESSAGE
root=Tk()
labelfont=('times', 20, 'bold')   
root.title('Success Confirmation')   
successText='Your update was successful'             
widget=Label(root, text=successText, wraplength=600, justify=LEFT)
widget.config(height=35, width=90)
widget.pack(expand=YES, fill=BOTH)
root.mainloop()

