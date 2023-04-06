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


window.mainloop()
