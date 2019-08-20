from tkinter import *
from tkinter import font


class Play(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#FFFFFF')

        self.currScore = 0

        # ---- Top Frame ----
        self.top_frame = Frame(self)
        self.color_top_frame = "#AABBCC"
        self.top_frame.configure(background=self.color_top_frame)
        self.top_frame.pack(side=TOP, fill='x', ipady='3m')

        self.img_home = PhotoImage(file="Image/pause.png").subsample(8)
        self.btn_home = Button(self.top_frame, image=self.img_home, command=lambda: controller.show_frame("Home"))
        #self.btn_home = Button(self.top_frame, image=self.img_home, command=self.change_current_score)
        self.btn_home.configure(borderwidth='0', activebackground=self.color_top_frame, background=self.color_top_frame)
        self.btn_home.pack(side=RIGHT, padx='6m')

        self.font_score = font.Font(self, family='Arial', size=15, weight='bold')
        self.lbl_score = Label(self.top_frame, text="SCORE     "+str(self.currScore),
                               background=self.color_top_frame, font=self.font_score)
        self.lbl_score.pack(side=LEFT, padx='6m')

        # ---- Play Screen ----
        self.play_frame = Frame(self)
        self.play_frame.configure(background='#FFFFFF')
        self.play_frame.pack(expand=TRUE, fill='both')

    def update_score(self, value):
        # add 'value' amount to current score and update score label
        self.currScore += value
        self.lbl_score.configure(text='SCORE     '+str(self.currScore))
        print('current score : ' + str(self.currScore))