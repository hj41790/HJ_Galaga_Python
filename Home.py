from tkinter import *
from tkinter import font


class Home(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#FFFFFF')

        # ---- power frame -----
        self.title_font = font.Font(self, size=50, weight='bold')
        self.title_label = Label(self, text="GALAGA", background="#FFFFFF", font=self.title_font)
        self.title_label.pack(side=TOP, pady='50m')

        # ---- button frame ----

        self.btn_frame = Frame(self)
        self.btn_frame.configure(background='#FFFFFF')
        self.btn_frame.pack(side=BOTTOM, expand=YES, fill='both')

        self.btn_font = font.Font(self, family='Arial', size=15, weight='bold')

        self.btn_start = Button(self.btn_frame, text='GAME START', command=lambda: controller.show_frame("Play"))
        self.btn_start.configure(font=self.btn_font, borderwidth='0', activebackground='#FFFFFF', background='#E0E0E0', width=20)
        self.btn_start.pack(pady='3m', ipady='3m')

        self.btn_score = Button(self.btn_frame, text='SCORE', command=lambda: controller.show_frame("Score"))
        self.btn_score.configure(font=self.btn_font, borderwidth='0', activebackground='#FFFFFF', background='#E0E0E0', width=20)
        self.btn_score.pack(pady='3m', ipady='3m')
        
        self.btn_score = Button(self.btn_frame, text='EXIT', command=lambda: self.controller.destroy())
        self.btn_score.configure(font=self.btn_font, borderwidth='0', activebackground='#FFFFFF', background='#E0E0E0', width=20)
        self.btn_score.pack(pady='3m', ipady='3m')

    
    def ready(self):
        return