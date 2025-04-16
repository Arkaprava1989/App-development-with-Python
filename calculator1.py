from tkinter import * 
import pypopulation
root = Tk()
root.title ("Calculator")
# for making an entry widget
r = Entry(root, width =50, borderwidth = 5, bg = "white", fg= "blue")
#r.insert(0, "Enter the text") for a text to appear at the widget
r.grid(row =0, column =0, columnspan= 4, padx=10, pady=10)

def MyClick(digit):
    write = r.get()
    r.delete(0, END)
    #global x
    r.insert(0, str(write)+ str(digit))
def addition():
    first_number = r.get()
    global X
    global math
    math = "addition" 
    X= int(first_number)
    r.delete(0, END)
       

def subtraction():
    first_number = r.get()
    global X
    global math
    math = "subtraction"
    X= int(first_number)
    r.delete(0, END)
def divide():
    first_number = r.get()
    global X
    global math
    math = "divide" 
    X= int(first_number)
    r.delete(0, END)
def multiplication():
    first_number = r.get()
    global X
    global math
    math = "multiplication" 
    X= int(first_number)
    r.delete(0, END)


def equality():
    second_number = r.get()
    r.delete(0, END)
    if math == "addition":
        r.insert (0, X + int(second_number))
    elif math == "subtraction":
        r.insert(0, X - int(second_number))
    elif math == "divide" and int(second_number) != 0:
        r.insert(0, X/int(second_number))
    elif math == "multiplication":
        r.insert(0, X * int(second_number))
    elif math =="divide" and int(second_number) == 0:
        r.insert(0, str("infinite"))

def clear():
    r.delete(0, END)
# Define buttons:
MyButton1 = Button(root, text = "1", padx= 20, pady=10, command = lambda: MyClick(1))
MyButton2 = Button(root, text ="2", padx = 20, pady=10, command = lambda: MyClick(2))
MyButton3 = Button(root, text="3", padx=20, pady=10, command = lambda:MyClick(3))
MyButton4 = Button(root, text ="4", padx= 20, pady=10, command= lambda: MyClick(4))
MyButton5 = Button(root, text ="5", padx= 20, pady = 10, command = lambda: MyClick(5))
MyButton6 = Button(root, text = "6", padx=20, pady= 10, command = lambda: MyClick(6))
MyButton7 = Button(root, text = "7", padx=20, pady= 10, command = lambda: MyClick(7))
MyButton8 = Button(root, text = "8", padx=20, pady= 10, command = lambda: MyClick(8))
MyButton9 = Button(root, text = "9", padx=20, pady= 10, command = lambda: MyClick(9))
MyButton0 = Button(root, text = "0", padx=20, pady= 10, command = lambda: MyClick(0))
addition = Button(root, text= "+", padx =20, pady=10, command = addition)
subtraction =  Button(root, text = "-", padx = 20, pady =10, command = subtraction)
divide = Button(root, text = "/", padx =20, pady =10, command = divide)
multiplication = Button(root, text = "*", padx=20, pady=10, command = multiplication)
equality =  Button(root, text = "=", padx =20, pady =10, command = equality )
clear = Button(root, text = "clear", padx=10, pady=10, command = clear)

MyButton1.grid(row=1, column=0)
MyButton2.grid(row=1, column=1)
MyButton3.grid(row=1, column=2)
MyButton4.grid(row=1, column =3)
MyButton5.grid(row=2, column =0)
MyButton6.grid(row=2, column=1)
MyButton7.grid(row=2, column=2)
MyButton8.grid(row=2, column= 3)
MyButton9.grid(row=3, column=0)
MyButton0.grid(row=3, column=1)
addition.grid(row =3, column =2)
subtraction.grid(row =3, column =3)
divide.grid(row=4, column=0)
multiplication.grid(row=4, column=1)
equality.grid(row=4, column=2)
clear.grid(row=4, column=3)
root.mainloop()