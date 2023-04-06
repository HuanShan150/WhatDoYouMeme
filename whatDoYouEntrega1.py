from tkinter import *

class Main():
    def __init__ (self):
        self.mainWindow = Tk();
        self.mainWindow.title("What Do You Meme");
        self.mainWindow.geometry("1075x915");
        self.mainWindow.resizable(False, False);
        self.mainWindow["bg"]="gray";

        self.backGround = PhotoImage(file = "imagens/doge.gif")
        self.meme = PhotoImage(file = "imagens/meme.gif")
        self.whiteCard1 = PhotoImage(file = "imagens/white-card.gif", height=270, width=200)
        self.whiteCard2 = PhotoImage(file = "imagens/white-card.gif", height=270, width=200)
        self.whiteCard3 = PhotoImage(file = "imagens/white-card.gif", height=270, width=200)
        self.whiteCard4 = PhotoImage(file = "imagens/white-card.gif", height=270, width=200)
        self.whiteCard5 = PhotoImage(file = "imagens/white-card.gif", height=270, width=200)

        self.limg = Label(self.mainWindow, i=self.backGround)

        menuFrame = Frame(self.mainWindow)
        menuFrame.pack(pady=5 ,padx=10)


        self.button = Button(menuFrame, text="Confirmar")
        self.button.grid(row=0, column=0)

        meme = Label(self.mainWindow, i=self.meme)
        meme.pack(pady=5 ,side= TOP)



        card1 = Label(self.mainWindow, i=self.whiteCard1)
        card2 = Label(self.mainWindow, i=self.whiteCard2)
        card3 = Label(self.mainWindow, i=self.whiteCard3)
        card4 = Label(self.mainWindow, i=self.whiteCard4)
        card5 = Label(self.mainWindow, i=self.whiteCard5)
        card1.pack(padx=5, pady=15,side=LEFT)
        card2.pack(padx=5, pady=15,side=LEFT)
        card3.pack(padx=5, pady=15,side=LEFT)
        card4.pack(padx=5, pady=15,side=LEFT)
        card5.pack(padx=5, pady=15,side=LEFT)

        
        self.mainWindow.mainloop();

    def ooutro(self):
        print('oi');

Main();