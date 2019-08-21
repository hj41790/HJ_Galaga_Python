from tkinter import *
from tkinter import font


class Score(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#FFFFFF')

        self.list_rank_text = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']

        # ---- Top Frame ----
        self.top_frame = Frame(self)
        self.color_top_frame = "#ABCDEF"
        self.top_frame.configure(background=self.color_top_frame)
        self.top_frame.pack(side=TOP, fill='x')

        self.img_home = PhotoImage(file="Image/home.png").subsample(8)
        self.btn_home = Button(self.top_frame, image=self.img_home, command=lambda: controller.show_frame("Home"))
        self.btn_home.configure(borderwidth='0', activebackground=self.color_top_frame, background=self.color_top_frame)
        self.btn_home.pack(side=RIGHT, padx='6m', pady='6m', anchor='ne')

        self.title_font = font.Font(self, family='Arial', size=40, weight='bold')
        self.title_label = Label(self.top_frame, text="     SCORE", background=self.color_top_frame, font=self.title_font)
        self.title_label.pack(side=TOP, pady='20m')

        self.color_score_frame = "#ABCDEF"
        self.score_frame = Frame(self)
        self.score_frame.configure(background=self.color_score_frame)
        self.score_frame.pack(side=BOTTOM, expand=YES, fill='both')

        self.score_top_font = font.Font(self, family='Consolas', size=18, weight='bold')
        self.score_btm_font = font.Font(self, family='Consolas', size=15)
        self.list_score_label = list()
        for i in range(0, 3): self.list_score_label.append(Label(self.score_frame, background=self.color_score_frame, font=self.score_top_font))
        for i in range(3, 10): self.list_score_label.append(Label(self.score_frame, background=self.color_score_frame, font=self.score_btm_font))
        for i in range(0, 10): self.list_score_label[i].pack(side=TOP, pady='3m')

    def ready(self):
        list_score = list()
        
        f = open('.score', 'r')
        while True:
            line = f.readline()
            if not line: break
            name, value = line.split(',')
            list_score.append((name, int(value)))
        f.close()

        # ---- insert new record if exist ----
        if self.controller.info["score"] >= 0:
            new_score = (self.controller.info["username"], self.controller.info["score"])
            for i in range(0, 10):
                if i == len(list_score):
                    list_score.append(new_score)
                    break
                elif list_score[i][1] < new_score[1]:
                    list_score.insert(i, new_score)
                    break
        if len(list_score) > 10: del list_score[10]

        # ---- save score and map ranking text to label ----
        f = open('.score', 'w')
        for i in range(0, len(list_score)):
            f.write('%s,%d\n' % (list_score[i][0], list_score[i][1]))
            if i < 3:
                self.list_score_label[i].configure(text=('%4s %-15s %-10d' % (self.list_rank_text[i], list_score[i][0], list_score[i][1])))
            else:
                self.list_score_label[i].configure(text=('%5s %-18s %-12d' % (self.list_rank_text[i], list_score[i][0], list_score[i][1])))
        f.close()

        print('score list :', list_score)