from tkinter import *
from random import *

win = Tk()
win.grid_columnconfigure(1, weight=1)
win.title('Nostravramus')
win.attributes("-fullscreen", True)


def submit():
    Label(win, text='\n                                ').grid(row=6, column=1)
    d = c.get()
    global b
    b = int(d)
    global k
    if b == a:
        Label(win, text='Ai ghicit numărul!').grid(row=6, column=1)
        return 0
    if b < a:
        Label(win, text='\nMai mare').grid(row=6, column=1)
        c.delete(0, END)
    else:
        Label(win, text='\nMai mic').grid(row=6, column=1)
        c.delete(0, END)
    k -= 1
    if k > 1:
        Label(win, text='\n                                ').grid(row=7, column=1)
        Label(win, text='\nMai ai ' + str(k) + ' vieți\n').grid(row=7, column=1)
    elif k == 1:
        Label(win, text='\n                                ').grid(row=7, column=1)
        Label(win, text='\nMai ai o viață!').grid(row=7, column=1)
    if k == 0:
        Label(win, text='\n                                ').grid(row=6, column=1)
        Label(win, text='\n                                ').grid(row=7, column=1)
        Label(win, text='Ai pierdut! Numărul căutat era ' + str(a)).grid(row=6, column=1)
        c.delete(0, END)
        return 0

def restart():
    c.delete(0, END)
    Label(win, text='                    \n                          ').grid(row=6, column=1)
    Label(win, text='                                              ').grid(row=7, column=1)
    a = randrange(1000)
    global k
    k=15

def exit_app():
    win.destroy()

sp = Label(win, text='\n')
a = randrange(1000)
c = Entry(win, width=10, borderwidth=5)
c.grid(row=3, column=1)
print(a)
sp1 = Label(win, text='\n')
sp1.grid(row=4, column=0)

global k
k=15

sp = Label(win, text='\n')
sp.grid(row=0, column=0)
title = Label(win, text='Ghicește numărul', font=('helvetica12', 24)).grid(row=1, column=1)
descr = Label(win, text='(numărul e cuprins între 0 și 1000)\n', font=('helvetica12', 10)).grid(row=2, column=1)
subm = Button(win, text='Apasă', command=submit).grid(row=5, column=1)
Label(win, text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n').grid(row=8, column=1)
restart = Button(win, text='Reset', command=restart, padx='50', pady='20').grid(row=9, column=1)
Label(win, text='\n').grid(row=10, column=1)
subm = Button(win, text='Exit', command=exit_app, padx='30', pady='20').grid(row=11, column=1)
win.mainloop()
