from c4_brain import ConnectFour
from tkinter import *
from tkinter import ttk


class Game(object):
    def __init__(self, root):
        self.root = root
        self.column_width = 100
        self.row_height = 100
        self.init_window()
        self.init_grid(self.window_canvas, self.column_width, self.row_height)
        self.get_mouse_x_coord()
        self.connectFourObj = ConnectFour()

    def init_window(self):
        self.root.title('Connect 4 Game')
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.columnconfigure(5, weight=1)
        self.root.columnconfigure(6, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.canvas_width = 700
        self.canvas_height = 600
        self.window_canvas = Canvas(
            self.root, width=self.canvas_width, height=self.canvas_height, background='#e6e6e6')
        self.window_canvas.grid(column=0, row=0)

    def init_grid(self, canvas, column_width, row_height):
        for x in range(column_width, self.canvas_width, column_width):
            canvas.create_line(x, 0, x, self.canvas_height,
                               fill='#1d66db', width=2,)

        for y in range(row_height, self.canvas_width-100, row_height):
            canvas.create_line(0, y, self.canvas_width,
                               y, fill='#1d66db', width=2)

    def draw_circle(self, color, start_coords, end_coords):
        self.window_canvas.create_oval(
            start_coords[0]+10, start_coords[1]+10, end_coords[0]-10, end_coords[1]-10, fill=color)

    def get_mouse_x_coord(self):
        self.window_canvas.bind(
            '<Button-1>', lambda e: self.where_to_draw(e.x))

    def where_to_draw(self, x_coord):
        column = x_coord//self.column_width
        row = self.connectFourObj.next_spot(column)
        if row != None:
            start_coords = ((column*self.column_width), (row*self.row_height))
            end_coords = ((column*self.column_width)+self.column_width,
                          (row*self.row_height)+self.row_height)
            self.draw_circle('red', start_coords, end_coords)
            print('Drawnnnn')
        else:
            pass


root = Tk()
Game(root)
root.mainloop()
