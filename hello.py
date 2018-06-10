#!/usr/bin/env python
# coding=utf-8

import sys
from tkinter import *

def open():
    print('Welcome !')
    sys.open()

def exit():
    print('Thanks For Using !')
    sys.exit()

Widget = Button(None, Text='Hello !', COMMAND=sys.open)
Widget = Button(None, Text='Good Bye !', COMMAND=sys.exit)
Widget.pack()
Widget.mainloop()