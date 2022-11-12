from tkinter import *
import random
from tkinter import messagebox


def play(height, width, mines):
    root = Tk()
    root.title("Minesweeper")
    root.geometry("1000x800")
    root.configure(background="blue")

    difficulty_frame = Frame(root, bg="gray", pady=30)
    difficulty_frame.pack(fill=X)

    control_frame = Frame(root, bg="gray", pady=10)
    control_frame.pack(fill=X)

    game_frame = Frame(root, bg="white")
    game_frame.pack(expand=True, fill=BOTH)

    # make 4 difficulty buttons

    difficulty_frame.columnconfigure(0, weight=1)

    beginner = Button(difficulty_frame, text="beginner").grid(row=0, column=1)

    difficulty_frame.columnconfigure(2, weight=1)

    intermediate = Button(
        difficulty_frame, text="intermediate").grid(row=0, column=3)

    difficulty_frame.columnconfigure(4, weight=1)

    expert = Button(difficulty_frame, text="expert").grid(row=0, column=5)

    difficulty_frame.columnconfigure(6, weight=1)

    custom = Button(difficulty_frame, text="custom").grid(row=0, column=7)

    difficulty_frame.columnconfigure(8, weight=6)

    # make mine count restart button and timer

    control_frame.columnconfigure(0, weight=1)

    mine_num = Label(control_frame, text="###").grid(column=1, row=0)

    control_frame.columnconfigure(2, weight=4)

    restart = Button(control_frame, text="Restart").grid(column=3, row=0)

    control_frame.columnconfigure(4, weight=4)

    timer = Label(control_frame, text="###").grid(column=5, row=0)

    control_frame.columnconfigure(6, weight=1)

    root.mainloop()


play(1, 1, 1)
