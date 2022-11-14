import random
from tkinter import *
from tkinter import messagebox

#I feel bad about this but I'm going to make height width and mines globals to connect 
# between the button clicked and play functions I should do this with classes but I'm too lazy
# to fix that


class Globals ():
    height = 16
    width = 30
    mines = 99
    game_frame = None
    board = None
    x = 0
    y = 0




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
        for tile in self.tiles:
            if self.tiles[tile].mine:
                self.tiles[tile].config(bg='black')

    def win(self):
        self.gamewon = True
        for tile in self.tiles:
            if self.tiles[tile].mine:
                self.tiles[tile].config(text="F",bg="red")

                
        


class Tile(Label):
    def __init__(self,master,i, j, mine, mine_neighbors=NONE):
        Label.__init__(self,master,width=2,relief=RAISED)
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

               
    def flag_coordinates(self,event,i,j):
        Globals.y = i
        Globals.x = j


    def flag_place(self,event):
        if Globals.board.tiles[Globals.y,Globals.x].flagged == False and Globals.board.tiles[Globals.y,Globals.x].revealed == False:
            Globals.board.tiles[Globals.y,Globals.x].configure(bg="red", text="F")
            Globals.board.tiles[Globals.y,Globals.x].flagged = True
        elif Globals.board.tiles[Globals.y,Globals.x].revealed == False:
            Globals.board.tiles[Globals.y,Globals.x].configure(bg="white",text="")
            Globals.board.tiles[Globals.y,Globals.x].flagged = False


    def flag(self,event):
        if self.flagged == False and self.revealed == False:
            self.configure(bg="red", text="F")
            self.flagged = True
        elif self.revealed == False:
            self.configure(bg="white",text="")
            self.flagged = False
    
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
    Globals.height = 30
    Globals.width = 30
    Globals.mines = 150
    Globals.board.gamewon = None
    Globals.board.update_board(Globals.game_frame,Globals.height,Globals.width,Globals.mines)

def restart_clicked():
    Globals.board.gamewon = None
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

    restart = Button(control_frame, text="Restart", command=restart_clicked).grid(column=3, row=0)

    control_frame.columnconfigure(4, weight=4)

    timer = Label(control_frame, text="000").grid(column=5, row=0)

    control_frame.columnconfigure(6, weight=1)

    Globals.board = GameBoard(Globals.game_frame,Globals.height,Globals.width,Globals.mines)
    

    root.mainloop()



play()

