# Joes Car Shop
import tkinter as tk

window = tk.Tk()

window.geometry("800x800")
window.configure(bg = "red")

v = tk.IntVar()
v.set(1)


MENUSTUFF = [
        ("Oil Change", 26),
        ("Lube job", 18),
        ("Radiator flush", 30),
        ("Transmission flush", 80),
        ("Inspection", 15),
        ("Muffler Replacement", 100),
        ("Tire rotation", 20)
    ]
def ShowChoice():
    print(v.get())

def totalrip():
    totalripoff = 1000
    return totalripoff


def buyit():
    total = totalrip()
    cart = tk.Text(master=window, height=5, width=5,bg='red',fg='blue',font=50)
    cart.grid(column=0,row=10)
    cart.insert(tk.END, total)

title = tk.Label(text = "Tim's Auto-Rip Off", fg = 'blue', bg = 'red', font = 24)
title.grid(column=0, row=0)

for val, m in enumerate(MENUSTUFF):
    tk.Radiobutton(window,text=m,variable=v,
            command=ShowChoice,value=val,fg='blue',
            bg='red', font=18).grid()


button1 = tk.Button(text="Add to Cart", bg='blue', fg='red',command=buyit)
button1.grid()









window.mainloop()