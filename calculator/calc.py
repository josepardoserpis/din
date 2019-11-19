import tkinter

window = tkinter.Tk()
window.title("CALCULADORA")
window.geometry("500x400")
output = tkinter.Entry(window, font=('arial', 20, 'bold'), width=30,insertwidth=4, justify="right").place(x=10, y=60)
Button9=tkinter.Button(window, text="9", width=6, height=3).place(x=15, y=180)
Button8=tkinter.Button(window, text="8", width=6, height=3).place(x=105, y=180)
Button7=tkinter.Button(window, text="7", width=6, height=3).place(x=195, y=180)
Button_div=tkinter.Button(window, text="/", width=6, height=3).place(x=285, y=180)
Button_mc=tkinter.Button(window, text="MC", width=6, height=3).place(x=375, y=180)

Button6=tkinter.Button(window, text="6", width=6, height=3).place(x=15, y=240)
Button5=tkinter.Button(window, text="5", width=6, height=3).place(x=105, y=240)
Button4=tkinter.Button(window, text="4", width=6, height=3).place(x=195, y=240)
Button_mult=tkinter.Button(window, text="*", width=6, height=3).place(x=285, y=240)
Button_ms=tkinter.Button(window, text="MS", width=6, height=3).place(x=375, y=240)

Button3=tkinter.Button(window, text="3", width=6, height=3).place(x=15, y=300)
Button2=tkinter.Button(window, text="2", width=6, height=3).place(x=105, y=300)
Button1=tkinter.Button(window, text="1", width=6, height=3).place(x=195, y=300)
Button_rest=tkinter.Button(window, text="-", width=6, height=3).place(x=285, y=300)
Button_mr=tkinter.Button(window, text="MR", width=6, height=3).place(x=375, y=300)

window.mainloop()