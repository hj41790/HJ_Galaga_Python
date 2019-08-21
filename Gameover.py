from tkinter import *
from tkinter import font


class Gameover(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.color_bg = '#FFFFFF'
        self.color_point = '#ABCDEF'
        self.isFocused = False

        self.controller = controller
        self.configure(background=self.color_bg)

        self.title_font = font.Font(self, family='Arial', size=40, weight='bold')
        self.title_label = Label(self, text="GAME OVER", background=self.color_bg, font=self.title_font)
        self.title_label.pack(side=TOP, pady='30m')

        self.lbl_font = font.Font(self, family='Arial', size=18, weight='bold')
        self.iyn_label = Label(self, text="Insert Your Name", background=self.color_bg, font=self.lbl_font)
        self.iyn_label.pack(side=TOP)

        self.font_inputbox = font.Font(self, family='Arial', size=25, weight='bold')
        self.inputbox = Entry(self, borderwidth='0', background=self.color_point, font=self.font_inputbox)
        self.inputbox.configure(justify='center', insertwidth=6, insertontime=600, insertofftime=600)
        self.inputbox.bind("<Return>", self.savescore)
        self.inputbox.focus()
        self.inputbox.pack(pady='5m', ipady='5m')

        self.btn_font = font.Font(self, family='Arial', size=15, weight='bold')
        self.btn_skip = Button(self, text='SKIP', command=self.skip_savescore)
        self.btn_skip.configure(font=self.btn_font, borderwidth='0', activebackground='#FFFFFF', background='#E0E0E0')
        self.btn_skip.pack(side=BOTTOM, ipadx='30m', ipady='3m', pady='30m')

    def savescore(self, event):
        if self.isFocused:
            self.isFocused = False
            username = self.inputbox.get()
            if username == '': username = 'Unknown'
            self.controller.info["username"] = username
            self.controller.show_frame("Score")

    def skip_savescore(self):
        self.isFocused = False
        self.controller.info["username"] = None
        self.controller.info["score"] = -1
        self.controller.show_frame("Home")
    
    def ready(self):
        self.isFocused = True
        self.inputbox.delete(0, len(self.inputbox.get()))
