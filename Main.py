from tkinter import *
from Home import *
from Play import *
from Gameover import *
from Score import *


class Galaga(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.info = dict()
        self.info["username"] = 'hyejeong'
        self.info["score"] = -1

        #self.geometry('480x800+300+100')
        self.geometry('480x800+300+1000')
        self.title('HJ_Galaga_Python')
        self.configure(background='#FFFFFF')
        self.resizable(False, False)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Home, Play, Gameover, Score):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")
        #self.show_frame("Score")
        #self.show_frame("Gameover")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.ready()
        frame.tkraise()


if __name__ == "__main__":
    app = Galaga()
    app.mainloop()