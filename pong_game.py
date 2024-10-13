from tkinter import * 
from tkinter import messagebox
import time 
import random 

window = Tk()
window.title("Pong Game!")
window.resizable(0,0)
window.wm_attributes("-topmost", 1) #makes it so that this window is always on top of any others

canvas = Canvas(window, width = 600, height = 500, bg = "black", bd = 1, highlightthickness = 1)
canvas.grid(row = 1, column = 1)
canvas.create_line(300, 0, 300, 500, fill = "white")
score_label = canvas.create_text(300, 30, font = ("times", 40), text = "0 : 0", fill = "white")
window.update()


class Ball:

    def __init__(self, canvas, paddle1, paddle2, color):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.color = color
        self.id = canvas.create_oval(10,10, 30,30 , fill = self.color)
        self.canvas.move(self.id, 300, 300)
        starts = [-3,-2, -1 , 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[1]
        self.y = starts[2]
        self.score1 = 0 
        self.score2 = 0 
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

    def draw_ball(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 4
        if pos[3] >= self.canvas_height:
            self.y = -4
        if pos[0] <= 0:
            self.score2 += 1
            self.x = 4
            
            
window.mainloop()