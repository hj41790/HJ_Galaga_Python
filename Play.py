from tkinter import *
from tkinter import font
from GameBoard import *
import threading


class Play(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.color_bg = '#FFFFFF'
        self.isFocused = False
        self.game = None
        self.bug1 = PhotoImage(file="Image/bug1.png").subsample(4)
        self.bug2 = PhotoImage(file="Image/bug2.png").subsample(4)
        self.bullet = PhotoImage(file="Image/bullet.png").subsample(4)
        self.plane = PhotoImage(file="Image/plane.png").subsample(4)
        self.blank = PhotoImage(file="Image/blank.png").subsample(4)
        self.lst_image = (self.blank, self.plane, self.bullet, self.bug1, self.bug2)
        # 0, 1, 2, 3, 4

        self.controller = controller
        self.configure(background='#FFFFFF')

        self.currScore = 0
        self.bindscore = StringVar()
        self.bindscore.set(self.currScore)

        # ---- Top Frame ----
        self.top_frame = Frame(self)
        self.color_top_frame = "#AABBCC"
        self.top_frame.configure(background=self.color_top_frame)
        self.top_frame.pack(side=TOP, fill='x', ipady='5m')

        self.img_pause = PhotoImage(file="Image/pause.png").subsample(8)
        self.btn_pause = Button(self.top_frame, image=self.img_pause, command=self.stop_game)
        #self.btn_pause = Button(self.top_frame, image=self.img_home, command=self.update_score)
        self.btn_pause.configure(borderwidth='0', activebackground=self.color_top_frame, background=self.color_top_frame)
        self.btn_pause.pack(side=RIGHT, padx='8m')

        self.font_score = font.Font(self, family='Arial', size=18, weight='bold')
        self.lbl_score_text = Label(self.top_frame, text="SCORE", 
                                    background=self.color_top_frame, font=self.font_score)
        self.lbl_score_text.pack(side=LEFT, padx='6m')
        
        self.lbl_score = Label(self.top_frame, textvariable=self.bindscore,
                               background=self.color_top_frame, font=self.font_score)
        self.lbl_score.pack(side=LEFT, padx='6m')

        # ---- Play Screen ----
        self.play_frame = Frame(self)
        self.play_frame.configure(background=self.color_bg)
        self.play_frame.focus_set()
        self.play_frame.bind("<Left>", self.press_left)
        self.play_frame.bind("<Right>", self.press_right)
        self.play_frame.bind("<space>", self.press_space)
        self.play_frame.pack(expand=TRUE, fill='both', padx='6m', pady='6m')

        self.gameboard = list()
        for i in range(GameBoard.board_height):
            tmp_board = list()
            self.gameboard.append(tmp_board)
            for j in range(GameBoard.board_width):
                tmp = Label(self.play_frame, background=self.color_bg, image=self.bullet)
                tmp.grid(row=i, column=j)
                tmp_board.append(tmp)

    def press_left(self, event):
        print('input : left')
        self.game.move('left')

    def press_right(self, event):
        print('input : right')
        self.game.move('right')

    def press_space(self, event):
        print('input : space')
        self.game.move('shoot')

    def update_score(self, value):
        # add 'value' amount to current score and update score label
        self.currScore += value
        self.bindscore.set(self.currScore)
        print('current score : ' + str(self.currScore))

    def stop_game(self):
        self.controller.info["score"] = self.currScore
        self.isFocused = False
        self.controller.show_frame("Gameover")

    def refresh(self):
        self.game.lock.acquire()
        try:
            for i in range(GameBoard.board_height):
                for j in range(GameBoard.board_width):
                    if self.gameboard[i][j]["image"] != self.lst_image[self.game.board[i][j]]:
                        self.gameboard[i][j].configure(image=self.lst_image[self.game.board[i][j]])
        finally:
            self.game.lock.release()
        if self.isFocused:
            t = threading.Timer(0.05, self.refresh)
            t.daemon = True
            t.start()

    def ready(self):
        self.isFocused = True
        self.currScore = 0
        self.controller.info["username"] = None
        self.controller.info["score"] = self.currScore

        self.game = GameBoard(self)
        self.refresh()


