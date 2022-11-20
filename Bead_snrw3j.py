import atexit
from tkinter import *
from tkinter.ttk import *
from xml.etree.ElementTree import tostring
import Class

keret = Tk()
keret.title("Informacio felvetel")

mylist = []
inputszoveg = StringVar(keret)
listacurrentszoveg = StringVar(keret)



def Felvetel():
    mylist.append(inputszoveg.get())
    lista1['values']=mylist

def Torles():
    if(listacurrentszoveg.get() in mylist):
        mylist.remove(listacurrentszoveg.get())
    lista1['values']=mylist
    szoveg1.config(text="")


def LabelAtiras(event):
    szoveg1.config(text=listacurrentszoveg.get())

def FajlBetoltes():
    mylist.clear()
    with open('adat.txt', 'r+') as f:
        for line in f:
            mylist.append(line.strip("\n"))
        lista1['values']=mylist

def FajlMentes():
    with open('adat.txt', 'w') as f:
        for line in mylist:
            f.write(f"{line}\n")

def konyveles():
    konyv1=Class.Konyveles(len(mylist))
    with open('konyveles.txt', 'w') as f:
            f.write(str(konyv1.tombhossz))
    
    

gombfajlbetoltes = Button(keret,text = "Adat betoltese",command=FajlBetoltes)
gombfajlbetoltes.grid(row=0,column=0)

gombfajlmentes = Button(keret,text = "Adat mentese",command = FajlMentes)
gombfajlmentes.grid(row=1,column=0)

gomb1 = Button(keret,text="Felvetel",command = Felvetel)
gomb1.grid(row=2,column=0)

gomb2 = Button(keret,text="Torles",command = Torles)
gomb2.grid(row=3,column=0)


szovegmutato1 = Label(keret,text="Objektumlista ==>")
szovegmutato1.grid(row=0,column=1)
szovegmutato2 = Label(keret,text="Eppen kijelolt objektum ==>")
szovegmutato2.grid(row=1,column=1)
szovegmutato3 = Label(keret,text="Beviteli mezo ==>")
szovegmutato3.grid(row=2,column=1)


lista1 = Combobox(keret,textvariable=listacurrentszoveg)
lista1.grid(row=0,column=2)
lista1.bind('<<ComboboxSelected>>',LabelAtiras)

szoveg1 = Label(keret,text = "")
szoveg1.grid(row=1,column=2)

szovegbe1 = Entry(keret,textvariable = inputszoveg)
szovegbe1.grid(row=2,column=2)


keret.mainloop()
atexit.register(konyveles)