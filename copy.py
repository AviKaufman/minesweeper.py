import tkinter as tk
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

    # outer frame
    outer_frame = ttk.Frame(self, padding=(10, 10, 10, 10))
    outer_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    # button
    self.button = ttk.Button(outer_frame, text='Click Me')
    self.button['command'] = self.button_clicked
    self.button.pack()

    #inner frame

    inner_frame = ttk.Frame(self, padding=(10, 10, 10, 10))
    inner_frame.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))

    # button

    self.button = ttk.Button(inner_frame, text='Click Me')
    self.button['command'] = self.button_clicked
    self.button.pack()

  def button_clicked(self):
    showinfo(title='Information', message='Hello, Tkinter!')

if __name__ == "__main__":
  app = Game(10,10,10)
  app.mainloop()