from tkinter import *
from tkinter import font


class Gameover(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#FFFFFF')

        self.title_font = font.Font(self, family='Arial', size=40, weight='bold')
        self.title_label = Label(self, text="GAME OVER", background="#FFFFFF", font=self.title_font)
        self.title_label.pack(side=TOP, pady='30m')

        self.lbl_font = font.Font(self, family='Arial', size=18, weight='bold')
        self.iyn_label = Label(self, text="Insert Your Name", background="#FFFFFF", font=self.lbl_font)
        self.iyn_label.pack(side=TOP)

        self.font_inputbox = font.Font(self, family='Arial', size=25, weight='bold')
        self.inputbox = Entry(self, borderwidth='0', background='#FFFFFF', font=self.font_inputbox)
        self.inputbox.configure(justify='center', insertwidth=6, insertontime=600, insertofftime=600)
        self.inputbox.bind("<Return>", self.savescore)
        self.inputbox.focus()
        self.inputbox.pack(pady='5m', ipadx='2m')

        self.btn_font = font.Font(self, family='Arial', size=15, weight='bold')
        self.btn_start = Button(self, text='SKIP', command=lambda: controller.show_frame("Home"))
        self.btn_start.configure(font=self.btn_font, borderwidth='0', activebackground='#FFFFFF', background='#E0E0E0')
        self.btn_start.pack(side=BOTTOM, ipadx='30m', ipady='3m', pady='30m')


    def savescore(self, event):
        username = self.inputbox.get()
        self.controller.show_frame("Score")
        print("savescore   "+username)