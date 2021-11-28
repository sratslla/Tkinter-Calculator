import math
from tkinter import * 

#change

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
# e.insert(0, "Enter Your Name:")


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math 
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtration":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
    if math == "power":
        e.insert(0, f_num**int(second_number))
    return

def button_sub():
    first_number = e.get()
    global f_num
    global math 
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_mul():
    first_number = e.get()
    global f_num
    global math 
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_div():
    first_number = e.get()
    global f_num
    global math 
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_power():
    first_number = e.get()
    global f_num
    global math 
    math = "power"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_sqrt():
    first_number = e.get()
    e.delete(0, END)
    e.insert(0, int(first_number)**0.5)
    return

def button_factorial():
    first_number = e.get()
    e.delete(0, END)
    factorial = 1
    if int(first_number) == 0:
        e.insert(0, factorial)
    else:
        for i in range(1,int(first_number) + 1):
            factorial = factorial*i
        e.insert(0, factorial)
    return


button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1)).grid(row = 3, column = 0)
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2)).grid(row = 3, column = 1)
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3)).grid(row = 3, column = 2)
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4)).grid(row = 2, column = 0)
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5)).grid(row = 2, column = 1)
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6)).grid(row = 2, column = 2)
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7)).grid(row = 1, column = 0)
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8)).grid(row = 1, column = 1)
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9)).grid(row = 1, column = 2)
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0)).grid(row = 4, column = 1)

add_button = Button(root, text = "+", bg = "grey", fg = "white", padx = 40, pady = 20, command = button_add).grid(row = 1, column = 3)
sub_button = Button(root, text = "-", bg = "grey", fg = "white", padx = 40, pady = 20, command = button_sub).grid(row = 2, column = 3)
mul_button = Button(root, text = "*", bg = "grey", fg = "white", padx = 40, pady = 20, command = button_mul).grid(row = 3, column = 3)
div_button = Button(root, text = "/", bg = "grey", fg = "white", padx = 40, pady = 20, command = button_div).grid(row = 4, column = 3)
power_button = Button(root, text = "x^2", bg = "grey", fg = "white", padx = 30, pady = 20, command = button_power).grid(row = 4, column = 0)
sqrt_button = Button(root, text = "sqrt", bg = "grey", fg = "white", padx = 32, pady = 20, command = button_sqrt).grid(row = 4, column = 2)
factorial_button = Button(root, text = "!", bg = "grey", fg = "white", padx = 40, pady = 20, command =  button_factorial).grid(row = 4, column = 3)

equal_button = Button(root, text = "=", bg = "grey", fg = "white", padx = 94, pady = 20, command = button_equal).grid(row = 2, column = 4, columnspan = 2)
clear_button = Button(root, text = "CLEAR", bg = "grey", fg = "white", padx = 79, pady = 20, command = button_clear).grid(row = 1, column = 4, columnspan =2)


#myButton = Button(root, text = "Enter Your Name!", command=myClick)
#myButton.pack()


root.mainloop()



