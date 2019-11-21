# This is the salutations app will take in a name and randomly generate a
# greeting

import random
import tkinter as tk

# Window
window = tk.Tk()
window.title("Salutations")
window.geometry("400x400")

# Functions
def phrase_generator():
    # Create a list of phrases
    phrases = ["Hello ", "What's up ", "Howdy ", "Aloha "]
    # get name from entry field
    name = str(entry1.get())

    return random.choice(phrases) + name

def phrase_display():
    # get gretting from a phrase_generator
    greeting = phrase_generator()

    # This creates the text field with out greeting
    greeting_display = tk.Text(master=window, height=10, width=30)
    greeting_display.grid(column=0, row=3)

    greeting_display.insert(tk.END, greeting)


# Label
label1 = tk.Label(text="How you doin?")
label1.grid(column=0, row=0)

label2 = tk.Label(text="What is your name?")
label2.grid(column=0, row=1)

# Entry
# No arguments because we want to take user input
entry1 = tk.Entry()
entry1.grid(column=1, row=1)


# Button
button1 = tk.Button(text="Click me!", command=phrase_display, bg = "purple")
button1.grid(column=0, row=2)




window.mainloop()