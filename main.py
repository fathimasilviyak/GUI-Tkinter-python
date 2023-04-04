# import tkinter
# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side ="left")
#
#
#
#
# window.mainloop()

def my_function(a=1,b=2, c=3):
    print(a, b, c)

# my_function()
# my_function(4, 5, 6)
# my_function(a=7, c=8)

def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)
add(1,2,3)
add(1,4)