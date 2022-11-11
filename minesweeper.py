import random
from tkinter import *
from tkinter import ttk

# set up the frame work for GUI

root = Tk()
root.geometry("1000x800")
frame = Frame(root, width=1000, height=50)
frame.pack(expand=True, fill=BOTH)
difficultyframe = Frame(frame, bg="white", width=1000, height=50)
difficultyframe.pack(expand=True, fill=BOTH)

# make 4 difficulty buttons

beginner = ttk.Button(difficultyframe, text="Beginner").grid(column=1, row=1)

intermediate = ttk.Button(
    difficultyframe, text="Intermediate").grid(column=3, row=1)

Expert = ttk.Button(difficultyframe, text="Expert").grid(column=5, row=1)

custom = ttk.Button(difficultyframe, text="Custom").grid(column=7, row=1)

difficultyframe.grid_columnconfigure(0, weight=4)
difficultyframe.grid_columnconfigure(2, weight=1)
difficultyframe.grid_columnconfigure(4, weight=1)
difficultyframe.grid_columnconfigure(6, weight=1)
difficultyframe.grid_columnconfigure(8, weight=12)


difficultyframe.grid_rowconfigure(0, weight=1)
difficultyframe.grid_rowconfigure(2, weight=1)

# set up mine and time labels as well as reset button


menuframe = Frame(frame, bg="gray", width=800, height=20)
menuframe.pack(expand=True, fill=BOTH)

mineCount = Label(menuframe, text="# # #").grid(column=1, row=1)

restart = Button(menuframe, text="restart").grid(column=3, row=1)

timeCount = Label(menuframe, text="# # #").grid(column=5, row=1)

menuframe.grid_columnconfigure(0, weight=1)
menuframe.grid_columnconfigure(2, weight=10)
menuframe.grid_columnconfigure(4, weight=10)
menuframe.grid_columnconfigure(6, weight=1)


menuframe.grid_rowconfigure(0, weight=1)
menuframe.grid_rowconfigure(2, weight=1)

# game frame should hold all mines


gameframe = Frame(frame, bg="light gray", width=1000,
                  height=600, highlightthickness=20)
gameframe.config(highlightbackground="gray")


gameframe.pack(expand=True, fill=BOTH)

gameframe.grid_columnconfigure(0, weight=1)
gameframe.grid_rowconfigure(0, weight=1)

gameframe.grid_rowconfigure(0, weight=1)
gameframe.grid_rowconfigure(2, weight=1)


# initialize the game with rows columns and mines


# run the program
root.title("Game")
root.mainloop()
minesweap = Game(10, 10, 10)
minesweap.placeMines()
