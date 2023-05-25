#
import tkinter as tk
from tkinter import ttk

#We creat a fuction for event
def on_select(event):

        #Create an item that obtains the value from the selected item.
        selected_item = event.widget.get()
        print("Selected item:", selected_item)

#
root = tk.Tk()
root.title("Python is awesome")

#
Items = ["Item 1", "Item 2", "Item 3", "Item 4"]

combo_box = ttk.Combobox(root, values=items)

#The bind function will tie the selected item to the on_selected function.
combo_box.bind("<<ComboboxSelected>>", on_select)
#Pack the object to the screen with the Geometry manager.
combo_box.pack()

#Mainloop keeps the root parent winsow visible.
root.mainloop()