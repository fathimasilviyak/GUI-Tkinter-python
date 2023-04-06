from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# my_label['text'] = "New Text"
# my_label.config(text="New text")


# Button
def button_clicked():
    # my_label.config(text="Button got clicked")
    new_text = input_name.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
# button.pack(side="left")
button.grid(column=1, row=1)

# Entry
input_name = Entry(width=30)
# Add some text to begin with
input_name.insert(END, string="Some text")
# input_name.pack(side="left")
input_name.grid(column=2, row=2)

window.mainloop()
