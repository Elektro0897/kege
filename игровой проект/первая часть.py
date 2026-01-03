from tkinter import *
import time
import random
tk = Tk()
tk.title('game')
tk.resizable(False, False)
tk.wm_attributes('-topmost', True)
canvas = Canvas(tk, width=500, height=400, highlightthickness=False)
