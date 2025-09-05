from tkinter import*
import tkinter.messagebox

window = Tk()
window.geometry("500x400")
window.config(bg="blanchedalmond")
en = Entry(window,width=35,borderwidth=5,bg="lightblue",font="bold")
en.place(x=0,y=0)

#onclick Functionalities...
def onclick(number):
    res = en.get()     # Get current text from input
    en.delete(0, END)  # Clear the entry field
    en.insert(0, str(res) + str(number))  # Append clicked number
    
#First row...
b = Button(window,text="9",width = 6,borderwidth=3,command=lambda:onclick(9),bg="black",fg="white",font="bold")
b.place(x=10,y=50)

b = Button(window,text="8",width = 6,borderwidth=3,command=lambda:onclick(8),bg="black",fg="white",font="bold")
b.place(x=85,y=50)

b = Button(window,text="7",width = 6,borderwidth=3,command=lambda:onclick(7),bg="black",fg="white",font="bold")
b.place(x=160,y=50)

#operator functionalities...
def add():
    num1 = en.get()
    global math
    math = "Addition"
    global i 
    i = int(num1)
    en.delete(0, END)

b = Button(window,text="+",width = 6,borderwidth=3,command=add,bg="yellow",fg="black",font="bold")
b.place(x=235,y=50)

#Second row...
b = Button(window,text="6",width = 6,borderwidth=3,command=lambda:onclick(6),bg="black",fg="white",font="bold")
b.place(x=10,y=90)

b = Button(window,text="5",width = 6,borderwidth=3,command=lambda:onclick(5),bg="black",fg="white",font="bold")
b.place(x=85,y=90)

b = Button(window,text="4",width = 6,borderwidth=3,command=lambda:onclick(4),bg="black",fg="white",font="bold")
b.place(x=160,y=90)

#operator functionalities...
def sub():
    num1 = en.get()
    global math
    math = "Subtraction"
    global i 
    i = int(num1)
    en.delete(0, END)
    
b = Button(window,text="-",width = 6,borderwidth=3,command=sub,bg="yellow",fg="black",font="bold")
b.place(x=235,y=90)

#Third row...
b = Button(window,text="3",width = 6,borderwidth=3,command=lambda:onclick(3),bg="black",fg="white",font="bold")
b.place(x=10,y=130)

b = Button(window,text="2",width = 6,borderwidth=3,command=lambda:onclick(2),bg="black",fg="white",font="bold")
b.place(x=85,y=130)

b = Button(window,text="1",width = 6,borderwidth=3,command=lambda:onclick(1),bg="black",fg="white",font="bold")
b.place(x=160,y=130)


#Multiplication operator functionalities...
def mul():
    num1 = en.get()
    global math
    math = "Multiplication"
    global i 
    i = int(num1)
    en.delete(0, END)
    
b = Button(window,text="*",width = 6,borderwidth=3,command=mul,bg="yellow",fg="black",font="bold")
b.place(x=235,y=130)

#Fouth row...

def clear():
    en.delete(0, END)
    
b = Button(window,text="CLEAR",width = 6,borderwidth=3,command=clear,bg="Red",fg="White",font="bold")
b.place(x=10,y=170)

b = Button(window,text="0",width = 6,borderwidth=3,command=lambda:onclick(0),bg="black",fg="white",font="bold")
b.place(x=85,y=170)


#eqaul operator functionalities...
def equal():
    n2 = en.get()
    en.delete(0, END)
    if math == "Addition":
        en.insert(0,i + int(n2))
    elif math == "Subtraction":
        en.insert(0,i - int(n2))
    elif math == "Multiplication":
        en.insert(0,i * int(n2))
    elif math == "Division":
        if int(n2) != 0:
            en.insert(0,i / int(n2))
        else:
            tkinter.messagebox.showerror("Divison Error","The first number can't be divided by the zero.")
            
b = Button(window,text="=",width = 6,borderwidth=3,command=equal,bg="green",fg="black",font="bold")
b.place(x=160,y=170)


#Division operator functionalities...
def div():
    num1 = en.get()
    global math
    math = "Division"
    global i 
    i = int(num1)
    en.delete(0, END)
    
b = Button(window,text="/",width = 6,borderwidth=3,command=div,bg="yellow",fg="black",font="bold")
b.place(x=235,y=170)

mainloop()