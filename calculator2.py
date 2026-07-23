import tkinter as tk

def analyz(char):
    
    if num1.get()=="" and char==".":
        return False
    if char.isdigit():
        return True
    elif char==".":
        if num1.get().count(".")==0 :
            return True
    return False

def analyz2(char2):
    if num2.get()=="" and char2==".":
        return False
    if char2.isdigit():
        return True
    elif char2==".":
        if num2.get().count(".")==0 :
            return True
    return False

def plus():
    try:
        a = float(num1.get())
        b = float(num2.get())
        result = a+b
        result_lable.config(text=f"result: {result}")
    except:
        result_lable.config(text="error! enter a number. ")

def minus():
    try:
        a = float(num1.get())
        b = float(num2.get())
        result = a-b
        result_lable.config(text=f"result: {result}")
    except:
        result_lable.config(text="error! enter a number. ")

def multipy():
    try:
        a = float(num1.get())
        b = float(num2.get())
        result = a*b
        result_lable.config(text=f"result: {result}")
    except:
        result_lable.config(text="error! enter a number. ")

def division():
    try:
        a = float(num1.get())
        b = float(num2.get())
        result = a/b
        result_lable.config(text=f"result: {result}")
    except:
        result_lable.config(text="error! enter a number. ")

root = tk.Tk()
root.title("calculator")
root.geometry("500x300")
root.configure(bg="#222021")

txt = tk.IntVar()
vcmd = (root.register(analyz), '%S')
vcmd2 = (root.register(analyz2), '%S')

num1 = tk.Entry(root, bg="#59575C", fg="white",font="Arial", width=5, validate="key", validatecommand=vcmd)
num1.place(x=50, y=100)

num2 = tk.Entry(root, bg="#59575C", fg="white",font="Arial", width=5, validate="key", validatecommand=vcmd2)
num2.place(x=150, y=100)

button1 = tk.Button(root, text="+", bg="#5A4A3E", fg="white", command=plus, font=("Arial", 14), width=3)
button1.place(x=50, y=180)

button2 = tk.Button(root, text="-", bg="#5A4A3E", fg="white", command=minus, font=("Arial", 14), width=3)
button2.place(x=100, y=180)

button3 = tk.Button(root, text="*", bg="#5A4A3E", fg="white", command=multipy, font=("Arial", 14), width=3)
button3.place(x=150, y=180)

button4 = tk.Button(root, text="/", bg="#5A4A3E", fg="white", command=division, font=("Arial", 14), width=3)
button4.place(x=200, y=180)

result_lable = tk.Label(root,text="result: ", bg="#88807B", fg="white", font=("Arial", 16))
result_lable.place(x=70, y=250)

root.mainloop()