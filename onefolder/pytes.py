import cv2
import pytesseract

import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk


class App:
    def __init__(self, root, msg):
        # setting title
        root.title("Editor")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.msg = msg
        L1 = Label(root, text=msg)
        L1.pack(side = TOP)
        self.entry = Entry(root)
        self.entry.focus_set()
        self.entry.pack()
        ttk.Button(root, text="Done", command=self.getvalue, width=20).pack(pady=20)

    def getvalue(self):
        res = self.entry.get()
        root.destroy()
        if res!=None:
            self.ret = res
        else:
            self.ret = self.msg











if __name__ == "__main__":
    img = cv2.imread('eq.png')

    pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/4.1.1/bin/tesseract'
    # Adding custom options
    custom_config = r'--oem 3 --psm 6'
    result = pytesseract.image_to_string(img, config=custom_config)
    root = tk.Tk()
    app = App(root, result)
    root.mainloop()