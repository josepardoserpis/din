from tkinter import ttk
from tkinter import *


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Boton que no hace nada")


root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=donothing)
filemenu.add_command(label="Abrir", command=donothing)
filemenu.add_command(label="Guardar", command=donothing)
filemenu.add_command(label="Guardar Como", command=donothing)
filemenu.add_command(label="Cerrar", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Deshacer", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cortar", command=donothing)
editmenu.add_command(label="Copiar", command=donothing)
editmenu.add_command(label="Pegar", command=donothing)
editmenu.add_command(label="Borrar", command=donothing)
editmenu.add_command(label="Seleccionar todo", command=donothing)

menubar.add_cascade(label="Editar", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
menu_ayu=Menu(menubar)
helpmenu.add_command(label="Indice de Ayuda", command=donothing)
helpmenu.add_command(label="Sobre...", command=donothing)
menubar.add_cascade(label="Ayuda", menu=menu_ayu)


root.config(menu=menubar)
root.mainloop()
