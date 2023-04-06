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
    new_text = input_name.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
input_name = Entry(width=30)
# Add some text to begin with
input_name.insert(END, string="Some text to begin with")
input_name.pack()

# Text
text = Text(height=5, width=30)
# Put cursor in text box
text.focus()
# Add some text to begin with
text.insert(END, "Some text for multi-line text entry")
# get hold of the text inside the text box starting from first line and zeroth character
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_clicked():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=10, command=spinbox_clicked)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbox
def checkbox_used():
    # print 1 if button is on otherwise 0
    print(checked_state.get())


# variable to hold on to checked state
checked_state = IntVar()
checkbox = Checkbutton(text="Is on?", variable=checked_state, command=checkbox_used)
print(checked_state.get())
checkbox.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="option2", value=2, variable=radio_state, command=radio_used)

radiobutton1.pack()
radiobutton2.pack()

window.mainloop()
