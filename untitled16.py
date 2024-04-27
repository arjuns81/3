from tkinter import *
import random

root=Tk()
root.title("Password Generator")
root.geometry("400x400")

label= Label(root)

array_3d =[[[1,2,3,4,5,6],["King","Queen"],["A","B","C","D","E","F","G","H"]]]
print(array_3d[0][2][3])

def new_password():
    random_no_1 = random.randit(0.5)
    random_no_2 = random.randit(0.1)
    random_no_3 = random.randit(0.7)


