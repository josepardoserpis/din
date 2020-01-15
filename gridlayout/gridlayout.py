import tkinter
from tkinter import ttk

window = ttk.tkinter.Tk()
lblgrid=list()

for i in range(4):
   lblgrid.append([])
   for c in range(4):
      ttk.Label(window, text='hola', borderwidth=15, background="red").grid(row=i, column=c)
window.mainloop()
#label02 = ttk.Label(frame,relief="ridge")
