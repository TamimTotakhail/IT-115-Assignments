#We import tkinter library here
import tkinter as tk

#We write a function for button click
def button_click():
    print("Button clicked!")
#We institiate the class library here
root = tk.Tk()
root.title("Button Example")

# We creat the button object
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

#
root.mainloop()

