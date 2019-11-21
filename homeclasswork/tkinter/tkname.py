# Access tkinter
import tkinter as tk

# instantiate a tkinter object
window = tk.Tk()

# Set the title
window.title("Name and Address")

# Set the size of your window
window.geometry("400x400")

def piI():
    info = "Ah ah ah, you didn't say the magic word."
    textbox = tk.Text(master=window, height=10, width=20)
    textbox.pack()
    textbox.insert(tk.END, info)
# adding a label
title= tk.Label(text = "Would you like to sell my PII? ")
title.pack()

#adding a button
button1= tk.Button(text="Click me for PII!", command=piI)
button1.pack()




window.mainloop()