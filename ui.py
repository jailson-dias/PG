#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()
root.title("PG 2016.2")
root.geometry("800x500+100+100")
slide_bar = Frame(root)


def params(master):
    global slide_bar

    l=Label(master,text="Coloque os valores para U0 ... Un")
    l.pack()
    slide_bar.pack(fill=X)
    # w = Scale(master, from_=1, to=200, orient=HORIZONTAL)
    # w.pack(fill=X)
    # b = Button(master, text='add', command=lambda: add())
    # b.pack()
    b=Button(master,text='Ok',command=lambda: get(slide_bar))
    b.pack()
    # b=Button(master,text='rm',command=lambda: remove(0))
    # b.pack()


def get(slide_bar):
    from hermite_bezier import paramentros
    parameter = []
    for i, v in enumerate(slide_bar.winfo_children()):
        parameter.append(v.winfo_children()[1].get())
    paramentros(parameter)

i = 0
def add():
    global slide_bar, i
    slide = Frame(slide_bar)
    slide.pack(fill=X)
    l = Label(slide, text="p" + str(i))
    l.pack(side=LEFT)
    w = Scale(slide, from_=1, to=30, orient=HORIZONTAL)
    w.pack(side=LEFT,expand=TRUE,fill=BOTH)
    i+=1

def remove(value):
    global slide_bar, i
    slide_bar.winfo_children()[value].destroy()
    i -= 1

def start():
    global root
    params(root)
    root.mainloop()

if __name__ == '__main__':
    start()