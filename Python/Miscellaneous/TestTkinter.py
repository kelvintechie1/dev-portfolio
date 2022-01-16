from tkinter import *
from tkinter import messagebox


def TPTSucks():
    messagebox.showinfo(title="More Cisco", message="TPT Sucks!")


window = Tk()
window.geometry("200x200")
killSwitch = Button(window, text="More Cisco!", command=TPTSucks, height=5, width=10)
killSwitch.pack()
window.mainloop()
