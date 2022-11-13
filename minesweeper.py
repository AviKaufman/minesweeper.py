import random
from tkinter import *
from tkinter import messagebox

#I feel bad about this but I'm going to make height width and mines globals to connect 
# between the button clicked and play functions I should do this with classes but I'm too lazy
# to fix that


class Globals ():
    height = 16
    width = 30
    mines = 10
    game_frame = None
    board = None



class GameBoard(Frame):
    def __init__(self, master, height, width, mines):
        Frame.__init__(self,master)
        self.master = master
        master.configure(bg="gray")
        master.pack(expand = True,fill = BOTH)
        self.game = Frame(master, bg="white",width = 800, height = 630)
        self.game.pack(expand=True)
        self.height = height
        self.width = width
        self.mines = mines

        self.tiles = {}

        for i in range(height):
            for j in range(width):
                self.tiles[i,j] = Tile(self.game,i,j,NONE)

    def update_board(self,master,height,width,mines):
        for i in range(height):
            for j in range(width):
                self.tiles[i,j] = Tile(self.game,i,j,NONE)
        


class Tile(Label):
    def __init__(self,master,i, j, mine, mine_neighbors=NONE):
        Label.__init__(self,master,width=2,relief=RAISED)
        self.grid(row=i,column=j)
        self.row = i
        self.column = j
    
    


def beginner_clicked():
    Globals.height = 10
    Globals.width = 10
    Globals.mines = 10
    Globals.board.update_board(Globals.game_frame,Globals.height,Globals.width,Globals.mines)

    
    

def intermediate_clicked():
    Globals.height = 16
    Globals.width = 16
    Globals.mines = 40
    Globals.board.update_board(Globals.game_frame,Globals.height,Globals.width,Globals.mines)

    
    

def expert_clicked():
    Globals.height = 16
    Globals.width = 30
    Globals.board.update_board(Globals.game_frame,Globals.height,Globals.width,Globals.mines)

    

def custom_clicked():
    Globals.height = 10
    Globals.width = 10
    Globals.mines = 10
    Globals.board.update_board(Globals.game_frame,Globals.height,Globals.width,Globals.mines)

    


def play():
    root = Tk()
    root.title("Minesweeper")
    root.geometry("1000x800")
    root.configure(background="blue")

    difficulty_frame = Frame(root, bg="gray", pady=20)
    difficulty_frame.pack(fill=X)

    control_frame = Frame(root, bg="gray", pady=20)
    control_frame.pack(fill=X)

    gray_frame = Frame(root, bg="gray")
    gray_frame.pack(expand=True, fill=BOTH)

    Globals.game_frame = Frame(gray_frame, bg="white", width=950, height=600)
    Globals.game_frame.pack(expand=True)

    # make 4 difficulty buttons

    difficulty_frame.columnconfigure(0, weight=1)

    beginner = Button(difficulty_frame, text="beginner", command = beginner_clicked).grid(row=0, column=1)

    difficulty_frame.columnconfigure(2, weight=1)

    intermediate = Button(
        difficulty_frame, text="intermediate", command=intermediate_clicked).grid(row=0, column=3)

    difficulty_frame.columnconfigure(4, weight=1)

    expert = Button(difficulty_frame, text="expert", command=expert_clicked).grid(row=0, column=5)

    difficulty_frame.columnconfigure(6, weight=1)

    custom = Button(difficulty_frame, text="custom", command=custom_clicked).grid(row=0, column=7)

    difficulty_frame.columnconfigure(8, weight=6)

    # make mine count restart button and timer

    control_frame.columnconfigure(0, weight=1)

    mine_num = Label(control_frame, text="099").grid(column=1, row=0)

    control_frame.columnconfigure(2, weight=4)

    restart = Button(control_frame, text="Restart").grid(column=3, row=0)

    control_frame.columnconfigure(4, weight=4)

    timer = Label(control_frame, text="000").grid(column=5, row=0)

    control_frame.columnconfigure(6, weight=1)

    Globals.board = GameBoard(Globals.game_frame,Globals.height,Globals.width,Globals.mines)
    

    root.mainloop()



play()
