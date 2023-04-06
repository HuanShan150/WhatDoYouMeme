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

        menuFrame = Frame( self.mainWindow, bg="gray", width= 10, height=30)
        menuFrame.pack(fill="both",ipady=3, ipadx=10)
        self.buttonStart = Button(menuFrame, text="Iniciar Jogo", width=10)
        self.buttonStart.grid(row=0, column=0, pady=2)
        self.buttonConnect = Button(menuFrame, text="Conectar", width=10)
        self.buttonConnect.grid(row=1, column=0, pady=2)
        self.buttonDisconect = Button(menuFrame, text="Desconectar", width=10)
        self.buttonDisconect.grid(row=2, column=0, pady=2)

        memeFrame = Frame(self.mainWindow, bg="gray", width= 10, height=30)
        memeFrame.pack(fill="x", ipady= 180)
        meme = Label(memeFrame, i=self.meme)
        meme.place(relx=0.5, rely=0.5, anchor=CENTER)

        
        cardsFrame = Frame(self.mainWindow, bg="gray", width= 10, height=30)
        cardsFrame.pack(fill="x", ipady= 5, side= BOTTOM)

        card1 = Label(cardsFrame, i=self.whiteCard1)
        card2 = Label(cardsFrame, i=self.whiteCard2)
        card3 = Label(cardsFrame, i=self.whiteCard3)
        card4 = Label(cardsFrame, i=self.whiteCard4)
        card5 = Label(cardsFrame, i=self.whiteCard5)
        card1.grid(row=0, column=0, padx=5, pady=3)
        card2.grid(row=0, column=1, padx=5, pady=3)
        card3.grid(row=0, column=2, padx=5, pady=3)
        card4.grid(row=0, column=3, padx=5, pady=3)
        card5.grid(row=0, column=4, padx=5, pady=3)

        self.buttonConfirm = Button(cardsFrame, text="Confirmar", width=10)
        self.buttonConfirm.grid(row=1, column=2, pady=2)


        self.mainWindow.mainloop();

    def ooutro(self):
        print('oi');

Main();