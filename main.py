from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()
# my_label['text'] = "New Text"
# my_label.config(text="New text")


# Button
def button_clicked():
    # my_label.config(text="Button got clicked")
    my_label.config(text=input_name.get())


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
input_name = Entry(width=10)
input_name.pack()

window.mainloop()
