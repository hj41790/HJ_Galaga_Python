from tkinter import *


class Score(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        """
        button1 = Button(self, text="Go to Page 1",
                         command=lambda: controller.show_frame("PageOne"))
        button2 = Button(self, text="Go to Page 2",
                         command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()
        """