import tkinter as tk


window = tk.Tk()

window.title("UFINDS")
window.geometry("775x519")
window.resizable(False, False)
window.iconbitmap("./assets/market.ico")

imageBackground = tk.PhotoImage(file="./assets/entrar.png")
iB= tk.Label(window, image=imageBackground)
iB.place(x=0,y=0)

def new_window():
    window.destroy()
    import login

imageButton = tk.PhotoImage(file="./assets/botaoEntrar.png")
iButton = tk.Button(window, image=imageButton, bd=0, bg='#FFFFFF', activebackground='#FFFFFF', command=new_window)
iButton.place(x=150,y=350)

window.mainloop()
