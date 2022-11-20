import random
import sched
import time
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.ttk import Combobox

from PIL import Image, ImageTk

#I feel bad about this but I'm going to make height width and mines globals to connect 
# between the button clicked and play functions I should do this with classes but I'm too lazy
# to fix that


class Globals ():
    height = 16
    width = 30
    mines = 99
    mine_count = 99
    difficulty_frame = None
    game_frame = None
    board = None
    x = 0
    y = 0
    control_frame = None
    time = 000
    game_started = False
    stop = True
    zoom = 20

    

    




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

        self.gamewon = None

        png = Image.open('flag.png')    #creating and storing flag and bomb images
        resize = png.resize((30,30), Image.Resampling.LANCZOS)
        self.flag = ImageTk.PhotoImage(resize)
        
        

        #create a list of mine values

        self.mine_grid = [[0]*width for i in [0]*height]
        while mines > 0:
            i = random.randint(0,height-1)
            j = random.randint(0,width-1)
            if self.mine_grid[i][j] == 0:
                self.mine_grid[i][j] = 1
                mines -= 1

        #create the board

        self.tiles = {}

        for i in range(height):
            for j in range(width):
                if self.mine_grid[i][j] == 1:
                    self.tiles[i,j] = Tile(self.game,i,j,True,NONE)
                else:
                    mine_neighbors = 0     #counting nearby mines if Tile in creation is not a mine
                    if i - 1 >= 0:
                        if self.mine_grid[i-1][j] == 1:
                            mine_neighbors += 1
                    if i - 1 >= 0 and j - 1 >= 0:
                        if self.mine_grid[i-1][j-1] == 1:
                            mine_neighbors += 1
                    if i - 1 >= 0 and j + 1 < width:
                        if self.mine_grid[i-1][j+1] == 1:
                            mine_neighbors += 1
                    if j - 1 >= 0:
                        if self.mine_grid[i][j-1] == 1:
                            mine_neighbors += 1
                    if j + 1 < width:
                        if self.mine_grid[i][j+1] == 1:
                            mine_neighbors += 1
                    if i + 1 < height:
                        if self.mine_grid[i+1][j] == 1:
                            mine_neighbors += 1
                    if i + 1 < height and j - 1 >= 0:
                        if self.mine_grid[i+1][j-1] == 1:
                            mine_neighbors += 1
                    if i + 1 < height and j + 1 < width:
                        if self.mine_grid[i+1][j+1] == 1:
                            mine_neighbors += 1
                    
                    self.tiles[i, j] = Tile(self.game, i, j, False, mine_neighbors)


    #update the board when game mode is changed

    def update_board(self,master,height,width,mines):
        Globals.game_started = False
        Globals.stop = True
        Globals.time = 000
        Globals.control_frame.grid_slaves(column = 5,row = 0)[0].configure(text ="{}".format(Globals.time).zfill(3))
        Globals.control_frame.grid_slaves(column = 1,row =0)[0].configure(text = "{}".format(Globals.mines))
        Globals.mine_count = Globals.mines
        self.game.destroy()
        Frame.__init__(self,master)
        self.master = master
        master.configure(bg="gray")
        master.pack(expand = True,fill = BOTH)
        self.game = Frame(master, bg="white",width = 800, height = 630)
        self.game.pack(expand=True)
        self.height = height
        self.width = width
        self.mines = mines


        png = Image.open('flag.png')    #creating and storing flag and bomb images
        resize = png.resize((30,30), Image.Resampling.LANCZOS)
        flag = ImageTk.PhotoImage(resize)
        


        #create a list of mine values

        self.mine_grid = [[0]*width for i in [0]*height]
        while mines > 0:
            i = random.randint(0,height-1)
            j = random.randint(0,width-1)
            if self.mine_grid[i][j] == 0:
                self.mine_grid[i][j] = 1
                mines -= 1

        #create the board

        self.tiles = {}


        for i in range(height):
            for j in range(width):
                if self.mine_grid[i][j] == 1:
                    self.tiles[i,j] = Tile(self.game,i,j,True,NONE)
                else:
                    mine_neighbors = 0     #counting nearby mines if Tile in creation is not a mine
                    if i - 1 >= 0:
                        if self.mine_grid[i-1][j] == 1:
                            mine_neighbors += 1
                    if i - 1 >= 0 and j - 1 >= 0:
                        if self.mine_grid[i-1][j-1] == 1:
                            mine_neighbors += 1
                    if i - 1 >= 0 and j + 1 < width:
                        if self.mine_grid[i-1][j+1] == 1:
                            mine_neighbors += 1
                    if j - 1 >= 0:
                        if self.mine_grid[i][j-1] == 1:
                            mine_neighbors += 1
                    if j + 1 < width:
                        if self.mine_grid[i][j+1] == 1:
                            mine_neighbors += 1
                    if i + 1 < height:
                        if self.mine_grid[i+1][j] == 1:
                            mine_neighbors += 1
                    if i + 1 < height and j - 1 >= 0:
                        if self.mine_grid[i+1][j-1] == 1:
                            mine_neighbors += 1
                    if i + 1 < height and j + 1 < width:
                        if self.mine_grid[i+1][j+1] == 1:
                            mine_neighbors += 1
                    
                    self.tiles[i, j] = Tile(self.game, i, j, False, mine_neighbors)


    def loss(self):
        self.gamewon = False
        Globals.stop = True
        Globals.game_started = False
        Globals.stop = True
        for tile in self.tiles:
            if self.tiles[tile].mine:
                self.tiles[tile].config(relief = SUNKEN, bg='black')

    def win(self):
        Globals.stop = True
        self.gamewon = True
        for tile in self.tiles:
            if self.tiles[tile].mine:
                self.tiles[tile].config(text="F",bg="red")

                
        


class Tile(Label):
    def __init__(self,master,i, j, mine, mine_neighbors=NONE):
        Label.__init__(self,master,width=2, height = 1, relief=RAISED, justify=CENTER)
        Globals.game_frame.option_add("*Font", "Helvetica {} bold".format(Globals.zoom))
        self.grid(row=i,column=j)
        self.row = i
        self.column = j
        self.mine = mine
        self.mine_neighbors = mine_neighbors
        self.revealed = False
        self.flagged = False
        self.flagged_neighbors = 0
        self.focus_set()
        self.bind("<Button-1>",self.reveal)
        self.bind("<Button-3>",self.flag)
        self.bind("<Button-2>",self.flag)
        self.bind("<Enter>",lambda event:self.flag_coordinates(event,self.row,self.column))
        self.bind("<space>",lambda event:self.flag_place(event))
        


    def reveal(self,event=None):
        if Globals.board.gamewon == None:
            if self.flagged == False:
                if self.mine == True:
                    self.configure(bg="black")
                    self.revealed = True
                    Globals.board.loss()
                else:
                    if self.mine_neighbors == 0:
                        self.configure(relief=SUNKEN,bg="light gray",text=" ")
                        self.revealed = True
                        self.reveal_neighbors(self.row,self.column)
                        
                        
                    #counting nearby mines if Tile in creation is not a mine
                    
                    
                    self.flagged_neighbors = 0
                    if self.row - 1 >= 0:
                        if (Globals.board.tiles[self.row-1,self.column].flagged == True):
                            self.flagged_neighbors +=1
                    if self.row - 1 >= 0 and self.column - 1 >= 0:        
                        if (Globals.board.tiles[self.row-1,self.column-1].flagged == True):
                            self.flagged_neighbors +=1
                    if self.row - 1 >= 0 and self.column + 1 < Globals.board.width:
                        if (Globals.board.tiles[self.row-1,self.column+1].flagged == True):
                            self.flagged_neighbors +=1
                    if self.column - 1 >= 0:
                        if (Globals.board.tiles[self.row,self.column-1].flagged == True):
                            self.flagged_neighbors +=1
                    if self.column + 1 < Globals.board.width:
                        if (Globals.board.tiles[self.row,self.column+1].flagged == True):
                            self.flagged_neighbors +=1
                    if self.row + 1 < Globals.board.height:
                        if (Globals.board.tiles[self.row+1,self.column].flagged == True):
                            self.flagged_neighbors +=1
                    if self.row + 1 < Globals.board.height and self.column - 1 >= 0:
                        if (Globals.board.tiles[self.row+1,self.column-1].flagged == True):
                            self.flagged_neighbors +=1
                    if self.row + 1 < Globals.board.height and self.column + 1 < Globals.board.width:
                        if (Globals.board.tiles[self.row+1,self.column+1].flagged == True):
                            self.flagged_neighbors +=1
                    
                    if self.flagged_neighbors == self.mine_neighbors and self.revealed == True:
                        self.reveal_neighbors(self.row,self.column)

                    #reveal value of tiles

                    else:
                        if self.mine_neighbors == 1:
                            self.configure(relief=SUNKEN, bg="light gray",text=self.mine_neighbors,fg="blue")
                            self.revealed = True
                            self.checkWin()
                        if self.mine_neighbors == 2:
                            self.configure(relief=SUNKEN,bg="light gray",text=self.mine_neighbors,fg="green")
                            self.revealed = True
                            self.checkWin()
                        if self.mine_neighbors == 3:
                            self.configure(relief=SUNKEN,bg="light gray",text=self.mine_neighbors,fg="red")
                            self.revealed = True
                            self.checkWin()
                        if self.mine_neighbors == 4:
                            self.configure(relief=SUNKEN,bg="light gray",text=self.mine_neighbors,fg="purple")
                            self.revealed = True
                            self.checkWin()
                        if self.mine_neighbors == 5:
                            self.configure(relief=SUNKEN,bg="light gray",text=self.mine_neighbors,fg="maroon")
                            self.revealed = True
                            self.checkWin()
                        if self.mine_neighbors == 6:
                            self.checkWin()
                            self.configure(relief=SUNKEN,bg="light gray",text=self.mine_neighbors,fg="teal")
                            self.revealed = True
                            self.checkWin()
                        if self.mine_neighbors == 7:
                            self.configure(relief=SUNKEN,bg="light gray",text=self.mine_neighbors,fg="Black")
                            self.revealed = True
                            self.checkWin()
                        if self.mine_neighbors == 8:    
                            self.configure(relief=SUNKEN,bg="light gray",text=self.mine_neighbors,fg="gray")
                            self.revealed = True  
                            self.checkWin()

                        if Globals.game_started == False:
                            Globals.stop = False
                            Globals.game_started = True
                            self.startClock()

    def startClock(self):
        if Globals.stop != True:
            Globals.time += 1
            Globals.control_frame.grid_slaves(column = 5,row = 0)[0].configure(text = "{}".format(Globals.time).zfill(3))
            Globals.control_frame.after(1000,self.startClock)


    def flag_coordinates(self,event,i,j):
        Globals.y = i
        Globals.x = j


    def flag_place(self,event):
        if Globals.board.gamewon == None:
            if Globals.board.tiles[Globals.y,Globals.x].flagged == False and Globals.board.tiles[Globals.y,Globals.x].revealed == False:
                Globals.board.tiles[Globals.y,Globals.x].configure(image = Globals.board.flag,padx = 12, pady = 12)
                Globals.board.tiles[Globals.y,Globals.x].flagged = True
                Globals.mine_count -= 1
                Globals.control_frame.grid_slaves(column = 1,row = 0)[0].configure(text = "{}".format(Globals.mine_count))
            elif Globals.board.tiles[Globals.y,Globals.x].revealed == False:
                Globals.board.tiles[Globals.y,Globals.x].configure(image = "",padx = 1,pady = 1)
                Globals.board.tiles[Globals.y,Globals.x].flagged = False
                Globals.mine_count += 1
                Globals.control_frame.grid_slaves(column = 1,row = 0)[0].configure(text = "{}".format(Globals.mine_count))


    def flag(self,event):
        if Globals.board.gamewon == None:
            if self.flagged == False and self.revealed == False:
                self.configure(bg="red", text="F")
                self.flagged = True
                Globals.mine_count -= 1
                Globals.control_frame.grid_slaves(column = 1,row = 0)[0].configure(text = "{}".format(Globals.mine_count))
            elif self.revealed == False:
                self.configure(bg="white",text="")
                self.flagged = False
                Globals.mine_count += 1
                Globals.control_frame.grid_slaves(column = 1,row = 0)[0].configure(text = "{}".format(Globals.mine_count))
    
    def reveal_neighbors(self,row,column):
        if row - 1 >= 0:
            if Globals.board.tiles[row-1,column].revealed == False:
                if Globals.board.tiles[row-1,column].flagged == False:
                    Globals.board.tiles[row-1,column].reveal()
        if row - 1 >= 0 and column - 1 >= 0:
            if Globals.board.tiles[row-1,column-1].revealed == False:
                if Globals.board.tiles[row-1,column-1].flagged == False:
                    Globals.board.tiles[row-1,column-1].reveal()
        if row - 1 >= 0 and column + 1 < Globals.width:
            if Globals.board.tiles[row-1,column+1].revealed == False:
                if Globals.board.tiles[row-1,column+1].flagged == False:
                    Globals.board.tiles[row-1,column+1].reveal()
        if column - 1 >= 0:
            if Globals.board.tiles[row,column-1].revealed == False:
                if Globals.board.tiles[row,column-1].flagged == False:
                    Globals.board.tiles[row,column-1].reveal()
        if column + 1 < Globals.width:
            if Globals.board.tiles[row,column+1].revealed == False:
                if Globals.board.tiles[row,column+1].flagged == False:
                    Globals.board.tiles[row,column+1].reveal()
        if row + 1 < Globals.height:
            if Globals.board.tiles[row+1,column].revealed == False:
                if Globals.board.tiles[row+1,column].flagged == False:
                    Globals.board.tiles[row+1,column].reveal()
        if row + 1 < Globals.height and column - 1 >= 0:
            if Globals.board.tiles[row+1,column-1].revealed == False:
                if Globals.board.tiles[row+1,column-1].flagged == False:
                    Globals.board.tiles[row+1,column-1].reveal()
        if row + 1 < Globals.height and column + 1 < Globals.width:
            if Globals.board.tiles[row+1,column+1].revealed == False:
                if Globals.board.tiles[row+1,column+1].flagged == False:
                    Globals.board.tiles[row+1,column+1].reveal()

    def checkWin(self):
        total_mines = Globals.board.mines
        total_tiles = Globals.width * Globals.height
        total_non_mines = total_tiles-total_mines
        for tile in Globals.board.tiles:
            if Globals.board.tiles[tile].revealed:
                total_non_mines -= 1
        if total_non_mines == 0:
            Globals.board.win()
    


def beginner_clicked():
    Globals.height = 10
    Globals.width = 10
    Globals.mines = 10
    Globals.board.gamewon = None
    Globals.board.update_board(Globals.game_frame,Globals.height,Globals.width,Globals.mines)
    
    

    
    

def intermediate_clicked():
    Globals.height = 16
    Globals.width = 16
    Globals.mines = 40
    Globals.board.gamewon = None
    Globals.board.update_board(Globals.game_frame,Globals.height,Globals.width,Globals.mines)
    
    
    

    
    

def expert_clicked():
    Globals.height = 16
    Globals.width = 30
    Globals.mines = 99
    Globals.board.gamewon = None
    Globals.board.update_board(Globals.game_frame,Globals.height,Globals.width,Globals.mines)
    

    

def custom_clicked():
    custom = askstring("Custom","Enter Height, Width, and Mines:")
    custom = custom.split()

    Globals.height = int(custom[0])
    Globals.width = int(custom[1])
    Globals.mines = int(custom[2])
    
    # Globals.height = 30
    # Globals.width = 30
    # Globals.mines = 150
    Globals.board.gamewon = None
    Globals.board.update_board(Globals.game_frame,Globals.height,Globals.width,Globals.mines)

def restart_clicked():
    Globals.board.gamewon = None
    Globals.board.update_board(Globals.game_frame,Globals.height,Globals.width,Globals.mines)

def zoom_clicked(self):
    text = Globals.difficulty_frame.grid_slaves(column = 9, row = 0)[0].get()
    if text == "1x":
        Globals.zoom = 10
    elif text == "2x":
        Globals.zoom = 15
    elif text == "3x":
        Globals.zoom = 20
    elif text == "4x":
        Globals.zoom = 25
    elif text == "5x":
        Globals.zoom = 30
    Globals.board.update_board(Globals.game_frame,Globals.height,Globals.width,Globals.mines)
    Globals.board.update_board(Globals.game_frame,Globals.height,Globals.width,Globals.mines)

    
    

    


def play():
    root = Tk()
    root.title("Minesweeper")
    root.geometry("1000x800")
    root.configure(background="blue")

    Globals.difficulty_frame = Frame(root, bg="gray", pady=20)
    Globals.difficulty_frame.pack(fill=X)

    Globals.control_frame = Frame(root, bg="gray", pady=20)
    Globals.control_frame.pack(fill=X)

    gray_frame = Frame(root, bg="gray")
    gray_frame.pack(expand=True, fill=BOTH)

    Globals.game_frame = Frame(gray_frame, bg="white", width=950, height=600)
    Globals.game_frame.pack(expand=True)

    # make 4 difficulty buttons

    Globals.difficulty_frame.columnconfigure(0, weight=1)

    beginner = Button(Globals.difficulty_frame, text="beginner", font= "Helvetica 10 bold", command = beginner_clicked).grid(row=0, column=1)

    Globals.difficulty_frame.columnconfigure(2, weight=1)

    intermediate = Button(
        Globals.difficulty_frame, text="intermediate", font= "Helvetica 10 bold", command=intermediate_clicked).grid(row=0, column=3)

    Globals.difficulty_frame.columnconfigure(4, weight=1)

    expert = Button(Globals.difficulty_frame, text="expert", font= "Helvetica 10 bold",  command=expert_clicked).grid(row=0, column=5)

    Globals.difficulty_frame.columnconfigure(6, weight=1)

    custom = Button(Globals.difficulty_frame, text="custom",font= "Helvetica 10 bold", command=custom_clicked).grid(row=0, column=7)

    Globals.difficulty_frame.columnconfigure(8, weight=3)

    zoom = Combobox(Globals.difficulty_frame, values=["1x", "2x", "3x","4x","5x"], font= "Helvetica 12 bold")
    zoom.set("zoom")
    zoom.bind('<<ComboboxSelected>>', zoom_clicked)
    zoom.grid(row=0, column=9)
    
    Globals.difficulty_frame.columnconfigure(10, weight=3)

    # make mine count restart button and timer

    Globals.control_frame.columnconfigure(0, weight=1)

    mine_num = Label(Globals.control_frame, text="099", font= "Helvetica 15 bold").grid(column=1, row=0)

    Globals.control_frame.columnconfigure(2, weight=4)

    restart = Button(Globals.control_frame, text="Restart", font= "Helvetica 10 bold", command=restart_clicked).grid(column=3, row=0)

    Globals.control_frame.columnconfigure(4, weight=4)

    timer = Label(Globals.control_frame, text="000", font= "Helvetica 15 bold").grid(column=5, row=0)

    Globals.control_frame.columnconfigure(6, weight=1)

    Globals.board = GameBoard(Globals.game_frame,Globals.height,Globals.width,Globals.mines)
    Globals.board.update_board(Globals.game_frame,Globals.height,Globals.width,Globals.mines)
    

    root.mainloop()



play()

