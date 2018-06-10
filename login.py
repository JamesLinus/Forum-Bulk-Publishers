from tkinter import *
from quitter import Quitter
fields = 'Name', 'Account', 'Password'

def  fetch(entries):
    for entry in entries:
        print('Input => "%s"' % entry.get())

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=5, text=field)
        ent = Entry(row)
        row.pack(side=TOP, fill=X)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expend=YES, fill=X)
        entries.append(ent)
    return entries

if __name__ == '__main__':
    root = TK()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda Event: fetch(ents)))
    Button(root, text='Fetch' ,
                  COMMAND= (lambda: fetch(ents))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.mainloop()