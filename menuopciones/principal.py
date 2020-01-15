from tkinter import ttk
from tkinter import *

root = Tk()


n = ttk.Notebook(root)
n.pack()

f1 = ttk.Frame(n)
f2 = ttk.Frame(n)
f3 = ttk.Frame(n)
f4 = ttk.Frame(n)

pest1 = ttk.Frame(f1)
pest2 = ttk.Frame(f2)

opc1 = ttk.Checkbutton(f1, text="Mostrar los numeros de linea")
opc1.pack()
opc2 = ttk.Checkbutton(f1, text="Mostrar margen derecho en la columna", )
opc2.pack()
opc3 = ttk.Checkbutton(f1, text="Mostrar barra de estado")
opc3.pack()
opc4 = ttk.Checkbutton(f1, text="Mostrar mapa de visión general")
opc4.pack()
opc5 = ttk.Checkbutton(f1, text="Mostrar cuadrícula")
opc5.pack()
lbl = Label(f1, text="Ajuste del texto", font=("Arial Bold", 18))
lbl.pack(side=LEFT, expand=YES)
opc6 = ttk.Checkbutton(f1, text="Activar ajuste de texto")
opc6.pack()
opc7 = ttk.Checkbutton(f1, text="No dividir palabras sobre dos lineas")
opc7.pack()
opc8 = ttk.Checkbutton(f1, text="Resaltar la línea actual")
opc8.pack()
opc9 = ttk.Checkbutton(f1, text="Resaltar parejas de corchetes")
opc9.pack()

n.add(f1, text='Ver')
n.add(f2, text='Editor')
n.add(f3, text='Tipografias y colores')
n.add(f4, text='Complementos')

root.mainloop()
