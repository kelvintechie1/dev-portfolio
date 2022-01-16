from tkinter import *
from tkinter.messagebox import *
from cml_et_breakout import *
from cml_et_apps import *
from PIL import Image, ImageTk


class toolGUI:
    def __init__(self, rootTk):
        self.rootTk = rootTk

        #rootTk.wm_geometry("700x700")
        rootTk.wm_title("CML Enhancement Tool v2")
        #rootTk.wm_resizable(False, False)

        self.toolLogo()
        self.createButtons()

    def testMessage(self):
        showinfo(message="Test")

    def testMessage2(self):
        showinfo(message="Test2")

    def createButtons(self):
        windowButtons = {}
        windowButtons["Open CML Main"] = Button(self.rootTk, text="Open CML Main", command=OpenCMLMain)
        windowButtons["Open CML Lab"] = Button(self.rootTk, text="Open CML Lab", command=OpenCMLLab)
        for button in windowButtons:
            windowButtons[button].pack()

    def toolLogo(self):
        logo = Image.open("CML Enhancement Tool v2.png")
        renderedLogo = ImageTk.PhotoImage(logo)
        logoObject = Label(self.rootTk, image=renderedLogo)
        logoObject.image = renderedLogo
        logoObject.pack()

    def titleLabel(self):
        label = Label(self.rootTk, "Hehe")
        label.pack()


def mainWindow():
    TkObject = Tk()
    guiObject = toolGUI(TkObject)
    TkObject.mainloop()
