from tkinter import *
from tkinter import ttk

# set up the frame work for GUI

root = Tk()
root.geometry("1000x800")
frame = Frame(root)

menuframe = Frame(root, bg="gray", width=1000, height=20)
menuframe.pack(expand=True, fill=BOTH)

mineCount = Label(menuframe, text="#").grid(column=1, row=1)

beginner = Button(menuframe, text="Beginner").grid(column=3, row=1)

intermediate = Button(menuframe, text="Intermediate").grid(column=4, row=1)

expert = Button(menuframe, text="Expert").grid(column=5, row=1)

custom = Button(menuframe, text="Custom").grid(column=6, row=1)

restart = Button(menuframe, text="restart").grid(column=8, row=1)

timeCount = Label(menuframe, text="#").grid(column=10, row=1)

menuframe.grid_columnconfigure(0, weight=1)
menuframe.grid_columnconfigure(2, weight=4)
menuframe.grid_columnconfigure(7, weight=2)
menuframe.grid_columnconfigure(9, weight=2)
menuframe.grid_columnconfigure(11, weight=1)

menuframe.grid_rowconfigure(0, weight=1)
menuframe.grid_rowconfigure(2, weight=1)


# menu frame should hold mine #, difficulty selection, restart button, and clock


gameframe = Frame(root, bg="light gray", width=1000,
                  height=650, highlightthickness=20)
gameframe.config(highlightbackground="gray")


gameframe.pack(expand=True, fill=BOTH)

height = 25
width = 25

gameframe.grid_columnconfigure(0, weight=1)
gameframe.grid_rowconfigure(0, weight=1)

gameframe.grid_columnconfigure(width+2, weight=1)
gameframe.grid_rowconfigure(height+2, weight=1)

for i in range(height):
    for j in range(width):
        button = Button(gameframe, width=2, height=1).grid(
            row=i+1, column=j+1)

# game frame should hold all mines


root.title("Game")
root.mainloop()
