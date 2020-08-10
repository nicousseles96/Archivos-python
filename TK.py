from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from os import path
raiz = Tk()
raiz.title("NO_SE_QUE_ESTOY_HACIENDO")
raiz.geometry('400x300')

#lbl = Label(raiz, text="HOLA", bg="blue", font=("Arial Bold", 20))
#lbl.grid(column=0, row=0)
#combo = Combobox(raiz)
#combo['values']= (1, 2, "s")
#combo.current(0)
#combo.grid(column=0, row=0)
#chk_state = IntVar()
#chk_state.set(True)
#chk = Checkbutton(raiz, text='presiona', var=chk_state)
#chk_state.set(1)	
#chk.grid(column=1, row=1)
#selec = IntVar()
#rad1 = Radiobutton(raiz,text='1', value=1, var=selec)
#rad2 = Radiobutton(raiz,text='2', value=2, var=selec)
#rad3 = Radiobutton(raiz,text='3', value=3, var=selec)
#def clc():
#	print(selec.get())
#btn = Button(raiz, text="hola", command=clc)
#btn.grid(column=0, row=2)	
#rad1.grid(column=1, row=0)
#rad2.grid(column=2, row=0)
#rad3.grid(column=3, row=0)
###
#var = IntVar()
#var.set(2)
#spin = Spinbox(raiz, values=(2, 4, 8), width=5, textvariable=var)
#spin.grid(column=0, row=0)
###
bar = Progressbar(raiz, length=200)
bar['value'] = 70	
bar.grid(column=0, row=1)
file = filedialog.askopenfilenames(initialdir= path.dirname(__file__), filetypes = (("JPG files","*.jpg"),("all files","*.*")))

print (file)
 
#txt = scrolledtext.ScrolledText(raiz, width=35, height=10)
#txt.insert(INSERT, 'holaaaaaaap')
#txt.delete(1.0,END)
#txt.grid(column=0,row=0)

####
#def clicked():
#	messagebox.askquestion('Titulo', 'Mesaje_Pregunta')
#   messagebox.askyesno('Titulo', 'Mesaje_SI-NO')
#   messagebox.askyesnocancel('Titulo', 'Mesaje_SI-NO-CANCEL')
#    messagebox.askokcancel('Titulo', 'Mesaje_OK-CANCEL')
#    messagebox.askretrycancel('Titulo', 'Mesaje_RETRY-CANCEL')

#    messagebox.showinfo('Titulo', 'Mesaje')
#    messagebox.showwarning('Titulo', 'Mesaje_Advertencia')
#    messagebox.showerror('Titulo', 'Mesaje_ERROR')
#btn = Button(raiz, text="Tocame", command=clicked)
#btn.grid(column=1, row=0)
####
#txt = Entry(raiz, width=10, state='disabled')
#txt.focus()
#txt.grid(column=0, row=1)
raiz.mainloop()
