

import tkinter as tk

window = tk.Tk()

window.title("UFINDS")
window.geometry("775x519")
window.resizable(False, False)

imageBackground = tk.PhotoImage(file="./assets/entrar.png")
iB= tk.Label(window, image=imageBackground)
iB.place(x=0,y=0)

imageButton = tk.PhotoImage(file="./assets/botaoEntrar.png")
iButton = tk.Button(window, image=imageButton, bd=0, bg='#FFFFFF', activebackground='#FFFFFF')
iButton.place(x=150,y=350)

window.mainloop()
