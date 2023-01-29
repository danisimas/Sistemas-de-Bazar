import tkinter as tk
from tkinter import ttk
import os
import csv

window = tk.Tk()
window.title("UFINDS")
window.geometry("775x519")
window.resizable(False, False)
window.iconbitmap("./assets/market.ico")

def open_profile():
    import profile_user
    
def exit_program():
    window.quit()


imageBackground = tk.PhotoImage(file="./assets/background.png")
iB= tk.Label(window, image=imageBackground)
iB.place(x=200,y=38, width=354)
menu = tk.Menu(window)
window.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Opções", menu=file_menu)
file_menu.add_command(label="Perfil", command=open_profile)
file_menu.add_separator()
file_menu.add_command(label="Sair", command=exit_program)


frameRecomendacoes = tk.Frame(window, bg="#6E9C7E", width=354, height=293)
frameRecomendacoes.place(x=19, y=188)

frame3 = tk.Frame(window, bg="#6E9C7E", width=354, height=293)
frame3.place(x=390, y=188)



window.mainloop()