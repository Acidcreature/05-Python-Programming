# access tkinter
import tkinter as tk

# instantiate a tkinter object
window = tk.Tk()

# Set the title
window.title("Latin Translator")

# Set window size
window.geometry("400x400")

# Add a label
title = tk.Label(text = "Latin Translator", font = ("Times New Roman", 22), width = 15)
title.grid(column=0, row=1,columnspan=10)

# Add a button
button1 = tk.Button(text = "sinister",width=10)
button1.grid(column=0,row=2,sticky='W',columnspan=10)

# Add a button
button2 = tk.Button(text = "dexter",width=10)
button2.grid(column=0,row=3,sticky='W',columnspan=10)

# Add a button
button3 = tk.Button(text = "medium",width=10)
button3.grid(column=0,row=4,sticky='W',columnspan=10)




window.mainloop()

