# -*- coding: utf-8 -*-
from tkinter import *
import time
import random


GUIDE = '''Click to start, wait for image and click to react.\n\
Don\'t click multiple times at once!!! or you have to wait.\n\
If you click before you should, results will be invalid.'''

ABOUT = '''A simple and crude reaction time tester.\n\
author: NitroMelon\n\
version: 0.1.0 2019.4.8'''

class ReactionTimer(object):
    
    def __init__(self, master=None):
        # main
        self.canvas = Canvas(master, width=200, height=100)
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.pack()
        self.is_running = False
        self.color = 'blue'
        self.reaction_time = 0
        
        # menu bar
        menu = Menu(master)
        master.config(menu=menu)
        colormenu = Menu(menu)
        menu.add_cascade(label='color', menu=colormenu)
        colormenu.add_command(label='blue', command=lambda: self.set_color('blue'))
        colormenu.add_command(label='red', command=lambda: self.set_color('red'))
        colormenu.add_command(label='green', command=lambda: self.set_color('green'))
        
        guidemenu = Menu(menu)
        menu.add_cascade(label='info', menu=guidemenu)
        guidemenu.add_command(label='guide', command=lambda: self.show_text(GUIDE))
        guidemenu.add_command(label='about', command=lambda: self.show_text(ABOUT))
        
        # status bar
        self.status = Label(master, text='Reaction time: unknown', bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    def set_color(self, color='blue'):
        self.color = color    
    
    def show_text(self, text):
        new_window = Toplevel()
        content = Label(new_window, text=text)
        content.pack()
        
    def on_click(self, e):
        if self.is_running:
            self.end()
        else:
            self.start()
        self.is_running = not self.is_running

    def start(self):
        time.sleep(1 + 5 * random.random())      
        # canvas
        self.r = self.canvas.create_rectangle(50, 25, 150, 75, fill=self.color, outline=self.color)  
        self.tstart = time.time()
   

    def end(self):
        self.tend = time.time()
        self.canvas.delete(ALL)
        self.reaction_time = self.tend - self.tstart
        # show info
        self.status.config(text='Reaction time: {:.3f}s'.format(self.reaction_time))


if __name__ == '__main__':
    root = Tk()
    root.title('Reaction Timer')
    root.resizable(0, 0)
    timer = ReactionTimer(root)
    root.mainloop()