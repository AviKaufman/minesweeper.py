import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


class Game(tk.Tk):
  def __init__(self,rows, columns, mines):
    super().__init__()
    self.rows = rows
    self.columns = columns
    self.mines = mines

    # configure the root window
    self.title('Minesweeper')
    self.geometry('800x600')

    main_frame = ttk.Frame(self)
    main_frame.pack(expand=True, fill= BOTH)

    # outer frame
    outer_frame = ttk.Frame(main_frame, width=800, height=20, padding=(10, 10, 10, 10))
    outer_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    # difficuclty buttons
    
    self.button = ttk.Button(outer_frame, text='Beginner')
    self.button['command'] = self.button_clicked
    self.button.pack(side='left')

    self.button = ttk.Button(outer_frame, text='Intermediate')
    self.button['command'] = self.button_clicked
    self.button.pack(side='left')

    self.button = ttk.Button(outer_frame, text='Expert')
    self.button['command'] = self.button_clicked
    self.button.pack(side='left')

    self.button = ttk.Button(outer_frame, text='Custom')
    self.button['command'] = self.button_clicked
    self.button.pack(side='left')

    #inner frame

    inner_frame = ttk.Frame(main_frame, padding=(10, 10, 10, 10))
    inner_frame.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))

    # button

    self.label = ttk.Label(inner_frame, text = "###").grid(column=1,row=0)

    self.button = ttk.Button(inner_frame, text='Restart')
    self.button['command'] = self.button_clicked
    self.button.grid(column = 3,row=0)

    self.label = ttk.Label(inner_frame, text = "###").grid(column=5,row=0)

    inner_frame.columnconfigure(0,weight=1)
    inner_frame.columnconfigure(2,weight=3)
    inner_frame.columnconfigure(4,weight=3)
    inner_frame.columnconfigure(6,weight=1)

  def button_clicked(self):
    showinfo(title='Information', message='Hello, Tkinter!')

if __name__ == "__main__":
  app = Game(10,10,10)
  app.mainloop()