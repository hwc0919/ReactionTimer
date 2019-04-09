# -*- coding: utf-8 -*-
#
# author: Nitro Melon
#
# change log:
# version 0.2.3 2019.4.9
#    fix a bug when cheating
# version 0.2.2 2019.4.8
#    edit guide and info messagebox
#    add icon
#    remove menu tearoff
#
# version 0.2.1 2019.4.8
#    show guide and about in messagebox
#
# version 0.2.0 2019.4.8
#    add multiple hints
#    improve click event logic and add cheat prompt
#
# version 0.1.0 2019.4.8


from tkinter import *
import threading
import time
import random
import tkinter.messagebox


GUIDE = '''Click to start, wait for image and click to react.\n\
Don't click multiple times at once!!!'''

ABOUT = '''A simple and crude reaction time tester.\n\
author: NitroMelon\n\
version: 0.2.3 2019.4.9'''


class ReactionTimer(object):
    
    def __init__(self, master):
        # main
        self.master = master
        self.master.title('Reaction Timer')
        self.master.iconbitmap('x:/projects/reaction_timer/xiguapig.ico')
        self.master.geometry('+800+400')
        self.master.resizable(0, 0)
        self.canvas = Canvas(master, width=200, height=100)
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.pack()
        self.state = 0
        self.color = 'blue'
        self.reaction_time = 0
        
        # menu bar
        menu = Menu(master)
        master.config(menu=menu)
        colormenu = Menu(menu, tearoff=0)
        menu.add_cascade(label='color', menu=colormenu)
        colormenu.add_command(label='blue', command=lambda: self.set_color('blue'))
        colormenu.add_command(label='red', command=lambda: self.set_color('red'))
        colormenu.add_command(label='green', command=lambda: self.set_color('green'))
        
        guidemenu = Menu(menu, tearoff=0)
        menu.add_cascade(label='info', menu=guidemenu)
        guidemenu.add_command(label='guide', command=lambda: self.show_text('guide'))
        guidemenu.add_command(label='about', command=lambda: self.show_text('about'))
        
        # status bar
        self.status = Label(master, text='click screen ONCE to start', bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    def set_color(self, color='blue'):
        self.color = color
    
    def show_text(self, text):
        if text == 'guide':
            tkinter.messagebox.showinfo(message=GUIDE, title='guide')
        elif text == 'about':
            tkinter.messagebox.showinfo(message=ABOUT, title='about')
        
    def on_click(self, e):
        if self.state == 0:
            self.thread = threading.Thread(target=self.start)
            self.thread.setDaemon(True)    #线程守护，即主进程结束后，此线程也结束。否则主进程结束子进程不结束
            self.thread.start()
        elif self.state == 1:
            self.state = -1
            tkinter.messagebox.showinfo(message='Don\'t cheat!', title='warning')
            self.canvas.delete(ALL)
            self.status.config(text='click screen ONCE to start')
            self.state = 0
        elif self.state == 2:
            self.end()

    def start(self):
        self.state = 1
        self.status.config(text='click when the image appears')
        wait_time = 1.5 + 2.5 * random.random()
        for i in range(int(wait_time * 10)):
            if self.state == 1:
                time.sleep(0.1)
            else:
                return

        # canvas
        if self.state == 1:
            self.r = self.canvas.create_rectangle(50, 25, 150, 75, fill=self.color, outline=self.color)  
            self.tstart = time.time()
            self.state = 2

    def end(self):
        self.tend = time.time()
        self.canvas.delete(ALL)
        self.reaction_time = self.tend - self.tstart
        # show info
        self.status.config(text='Reaction time: {:.3f}s'.format(self.reaction_time))
        self.state = 0


if __name__ == '__main__':
    root = Tk()
    timer = ReactionTimer(root)
    root.mainloop()
