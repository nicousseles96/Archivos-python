from tkinter import *
from tkinter import ttk
####    	
raiz = Tk()
raiz.title("Calculadora")
raiz.geometry('300x400')
raiz.resizable(False, False)
raiz.configure(bg="gray26")
####
color_boton="SteelBlue1"
ancho_boton=3
alto_boton=2
operador = ""
text_pat= StringVar()
def clear():
	global operador
	operador = ""
	text_pat.set("")
def click(bg):
	global operador
	operador += str(b)
	text_pat.set(operador)
def resultado():
	global operador
	try:
	   r = str(eval(operador))
	except:
	   r = "ERROR"
	text_pat.set(r)  
	    	
####
Boton0 = Button(raiz,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(7)).place(x=20,y=75)
Boton1 = Button(raiz,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(8)).place(x=90,y=75)
Boton2 = Button(raiz,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(9)).place(x=160,y=75)
BotonDEL = Button(raiz,text="DEl",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=230,y=75)
####
Boton3 = Button(raiz,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(4)).place(x=20,y=150)
Boton4 = Button(raiz,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(5)).place(x=90,y=150)
Boton5 = Button(raiz,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(6)).place(x=160,y=150)
BotonDIV = Button(raiz,text="÷",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("/")).place(x=230,y=150)
####
Boton6 = Button(raiz,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(1)).place(x=20,y=225)
Boton7 = Button(raiz,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(2)).place(x=90,y=225)
Boton8 = Button(raiz,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(3)).place(x=160,y=225)
BotonX = Button(raiz,text="x",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("X")).place(x=230,y=225)
####
BotonRES = Button(raiz,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("-")).place(x=20,y=300)
Boton9 = Button(raiz,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(0)).place(x=90,y=300)
BotonIGUA = Button(raiz,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=resultado).place(x=160,y=300)
BotonMAS = Button(raiz,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("+")).place(x=230,y=300)
####
pat = Entry(raiz, font=("arial",20,"bold"), width=16,borderwidth=10, bg="light coral",state="disabled",textvariable=text_pat)
pat.place(x=20,y=5)

######################################
 sudo dd if=/DISCO_MASTER  of=/DISCO_FINAL bs=64K conv=noerror,sync




raiz.mainloop()   

