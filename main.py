from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

# # Label
# my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# # my_label.pack()
# # my_label.place(x=0, y=0)
# my_label.grid(column=0, row=0)
#
# # Button
# def button_clicked():
#     # my_label.config(text="Button got clicked")
#     new_text = input_name.get()
#     my_label.config(text=new_text)
#
# button = Button(text="Click me", command=button_clicked)
# # button.pack(side="left")
# button.grid(column=1, row=1)
#
# # Entry
# input_name = Entry(width=30)
# # Add some text to begin with
# input_name.insert(END, string="Some text")
# # input_name.pack(side="left")
# input_name.grid(column=2, row=2)

my_label = Label(text="Label", font=("Arial", 20, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

button = Button(text="Button")
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

input_name = Entry()
input_name.grid(column=3, row=2)



window.mainloop()
