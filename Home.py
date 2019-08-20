from tkinter import *
from tkinter import font


class Home(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#FFFFFF')
        """
        button1 = Button(self, text="Go to Page 1",
                         command=lambda: controller.show_frame("PageOne"))
        button2 = Button(self, text="Go to Page 2",
                         command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()
        """

        # ---- power frame -----
        """
        self.image_off = PhotoImage(file="power_button.png").subsample(4)
        self.button0 = Button(self, image=self.image_off, command=self.closeFrame)
        self.button0.configure(borderwidth='0', activebackground="#FFFFFF", background="#FFFFFF")
        self.button0.pack(side=RIGHT)
        """
        self.title_font = font.Font(self, size=50, weight='bold')
        self.title_label = Label(self, text="GALAGA", background="#FFFFFF", font=self.title_font)
        self.title_label.pack(side=TOP, pady='50m')

        # ---- button frame ----

        self.btn_frame = Frame(self)
        self.btn_frame.configure(background='#FAFAFA')
        self.btn_frame.pack(side=BOTTOM, expand=YES, fill='both')

        self.btn_font = font.Font(self, family='Arial', size=15, weight='bold')

        self.btn_start = Button(self.btn_frame, text='GAME START', command=lambda: controller.show_frame("Play"))
        self.btn_start.configure(font=self.btn_font, borderwidth='0', activebackground='#FFFFFF', background='#E0E0E0')
        self.btn_start.pack(ipadx='10m', ipady='3m', pady='5m')

        self.btn_score = Button(self.btn_frame, text='SCORE', command=lambda: controller.show_frame("Score"))
        self.btn_score.configure(font=self.btn_font, borderwidth='0', activebackground='#FFFFFF', background='#E0E0E0')
        self.btn_score.pack(ipadx='18m', ipady='3m')