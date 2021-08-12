from tkinter import *
from bd_urna import *
from pygame import mixer
from threading import Timer

class Urna:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('900x500')
        self.root.title('Urna Eleitoral')
        self.total = ""
#---Labels---#
        self.lbl1 = Label(self.root, bg='#757575')
        self.lbl1.place(relx=0.5, rely=0, relheight = 1, relwidth = 0.5)
        self.lbl3 = Label(self.root, text = 'Seu voto para candidato:', font='arial, 20')
        self.lbl3.place(relx=0.03, rely=0.03)
        self.imgpreto = PhotoImage(file='preto.png')
        self.imglbl = Label(self.root, image=self.imgpreto)
        self.imglbl.place(relx=0.3, rely=0.15, height=150, width=150)
        self.nome = Label(self.root, text='Nome: ', font='arial 14', justify='center')
        self.nome.place(relx=0.05, rely=0.7)
        self.infolbl = Label(self.root, text='''
Aperte a tecla:
CONFIRMA para CONFIRMAR este voto
CORRIGE para REINICIAR este voto''', font='arial 14', justify=LEFT)
        self.infolbl.place(relx=0, rely=0.8)
        mixer.init()
        
#---Botões---#
        self.btn1 = Button(self.lbl1, text="1", font='arial 20', bg='black', activebackground = "black", fg='white', relief = 'ridge', command=lambda: self.clickNum(1))
        self.btn1.place(relx=0.02, rely=0.02, relheight = 0.15, relwidth = 0.3)
        self.btn2 = Button(self.lbl1, text="2", font='arial 20', bg='black', activebackground = "black", fg='white', relief = 'ridge', command=lambda: self.clickNum(2))
        self.btn2.place(relx=0.35, rely=0.02, relheight = 0.15, relwidth = 0.3)
        self.btn3 = Button(self.lbl1, text="3", font='arial 20', bg='black', activebackground = "black", fg='white', relief = 'ridge', command=lambda: self.clickNum(3))
        self.btn3.place(relx=0.68, rely=0.02, relheight = 0.15, relwidth = 0.3)
        self.btn4 = Button(self.lbl1, text="4", font='arial 20', bg='black', activebackground = "black", fg='white', relief = 'ridge', command=lambda: self.clickNum(4))
        self.btn4.place(relx=0.02, rely=0.2, relheight = 0.15, relwidth = 0.3)
        self.btn5 = Button(self.lbl1, text="5", font='arial 20', bg='black', activebackground = "black", fg='white', relief = 'ridge', command=lambda: self.clickNum(5))
        self.btn5.place(relx=0.35, rely=0.2, relheight = 0.15, relwidth = 0.3)
        self.btn6 = Button(self.lbl1, text="6", font='arial 20', bg='black', activebackground = "black", fg='white', relief = 'ridge', command=lambda: self.clickNum(6))
        self.btn6.place(relx=0.68, rely=0.2, relheight = 0.15, relwidth = 0.3)
        self.btn7 = Button(self.lbl1, text="7", font='arial 20', bg='black', activebackground = "black", fg='white', relief = 'ridge', command=lambda: self.clickNum(7))
        self.btn7.place(relx=0.02, rely=0.38, relheight = 0.15, relwidth = 0.3)
        self.btn8 = Button(self.lbl1, text="8", font='arial 20', bg='black', activebackground = "black", fg='white', relief = 'ridge', command=lambda: self.clickNum(8))
        self.btn8.place(relx=0.35, rely=0.38, relheight = 0.15, relwidth = 0.3)
        self.btn9 = Button(self.lbl1, text="9", font='arial 20', bg='black', activebackground = "black", fg='white', relief = 'ridge', command=lambda: self.clickNum(9))
        self.btn9.place(relx=0.68, rely=0.38, relheight = 0.15, relwidth = 0.3)
        self.btn0 = Button(self.lbl1, text="0", font='arial 20', bg='black', activebackground = "black", fg='white', relief = 'ridge', command=lambda: self.clickNum(0))
        self.btn0.place(relx=0.35, rely=0.56, relheight = 0.15, relwidth = 0.3)
        self.btnBranco = Button(self.lbl1, text="BRANCO", font='arial 16', bg='white', activebackground = "white", fg='black', relief = 'ridge', command=self.branco)
        self.btnBranco.place(relx=0.02, rely=0.75, relheight = 0.23, relwidth = 0.3)
        
        self.btnCorrige = Button(self.lbl1, text="CORRIGE", font='arial 16', bg='red', activebackground = "red", fg='black', relief = 'ridge', command=self.corrige)
        self.btnCorrige.place(relx=0.35, rely=0.75, relheight = 0.23, relwidth = 0.3)
 
        self.btnConfirma = Button(self.lbl1, text="CONFIRMA", font='arial 16', bg='green', activebackground = "green", fg='black', relief = 'ridge', command=self.confirmar)
        self.btnConfirma.place(relx=0.68, rely=0.75, relheight = 0.23, relwidth = 0.3)
        
#---Entry---#
        self.ent = Label(self.root, text='', font="arial 14", justify='center')
        self.ent.place(relx=0.05, rely=0.6)

        self.root.mainloop()

    def clickNum(self, n):
        if len(self.ent['text']) < 2:
            self.ent['text'] = self.ent['text']+str(n)
            id = self.ent['text']
            self.candidato = locCandi(id)
            if self.candidato == 0:
                self.nome['text'] = 'ERRADO'
                if len(self.ent['text']) == 2 and self.candidato == 0:
                    self.nome['text'] = 'VOTO NULO'
            else:
                f = selecFoto(self.ent['text'])
                self.img = PhotoImage(file=f'{f}')
                self.imglbl['image'] = self.img
                self.nome['text'] = str(self.candidato)
        else:
            pass

    def confirmar(self):
        if self.ent['text'] == '':
            if self.ent['text'] == '' and self.fim['text'] == 'VOTO BRANCO':
                print(self.ent['text'])
                addVoto(self.ent['text'])
                self.fim = Label(self.root, text='FIM', font='arial 50', borderwidth=4, relief='raised', justify=CENTER)
                self.fim.place(relx=0.04, rely=0.1, relheight=0.7, relwidth=0.45)

                mixer.music.load('somurna.mp3')
                mixer.music.play()
                self.btnBranco['state'] = DISABLED
                self.btnConfirma['state'] = DISABLED

                t = Timer(4, self.corrige)
                t.start()
            else:
                mixer.music.load('somurna.mp3')
                mixer.music.play()
                self.btnBranco['state'] = DISABLED
                self.btnConfirma['state'] = DISABLED

                t = Timer(4, self.corrige)
                t.start()
                pass
        elif self.nome['text'] == 'VOTO NULO':
            print(self.nome['text'])
            addVoto(self.nome['text'])
            self.fim = Label(self.root, text='FIM', font='arial 50', borderwidth=4, relief='raised', justify=CENTER)
            self.fim.place(relx=0.04, rely=0.1, relheight=0.7, relwidth=0.45)
            mixer.music.load('somurna.mp3')
            mixer.music.play()
            self.btnBranco['state'] = DISABLED
            self.btnConfirma['state'] = DISABLED

            t = Timer(4, self.corrige)
            t.start()
        else:
            print(self.ent['text'])
            addVoto(self.ent['text'])
            self.fim = Label(self.root, text='FIM', font='arial 50', borderwidth=4, relief='raised', justify=CENTER)
            self.fim.place(relx=0.04, rely=0.1, relheight=0.7, relwidth=0.45)
            mixer.music.load('somurna.mp3')
            mixer.music.play()
            self.btnBranco['state'] = DISABLED
            self.btnConfirma['state'] = DISABLED

            t = Timer(4, self.corrige)
            t.start()

    '''def teclado(self, n):
        if len(self.total) < 2:
            if self.total == "":
                self.x = self.ent.get()
            else:
                self.x = self.x
            if self.x == "0" and evento == 0:
                pass
            elif self.x == "0":
                self.x = ""
            self.ent.delete(0, END)
            self.ent.insert(END, self.x + str(evento.char))
            self.x = self.x + str(evento.char)
            self.total = self.total + str(evento.char)'''

    def corrige(self):
        try:
            if self.ent['text'] == 'VOTO BRANCO':
                self.ent['text'] = ''
                self.nome['text'] = 'Nome: '
                self.imglbl['image'] = self.imgpreto
                self.fim.destroy()
                self.b.destroy()
                self.btnBranco['state'] = NORMAL
                self.btnConfirma['state'] = NORMAL
            else:
                self.ent['text'] = ''
                self.nome['text'] = 'Nome: '
                self.imglbl['image'] = self.imgpreto
                self.fim.destroy()
                self.btnBranco['state'] = NORMAL
                self.btnConfirma['state'] = NORMAL
        except:
            self.ent['text'] = ''
            self.nome['text'] = 'Nome: '
            self.imglbl['image'] = self.imgpreto
            self.btnBranco['state'] = NORMAL
            self.btnConfirma['state'] = NORMAL

    def branco(self):
        self.b = Label(self.root, text='VOTO BRANCO', font='arial 30', borderwidth=4, relief='raised', justify=CENTER)
        self.b.place(relx=0.04, rely=0.1, relheight=0.7, relwidth=0.45)
        self.ent['text'] = 'VOTO BRANCO'

if __name__ == '__main__':
    Urna()