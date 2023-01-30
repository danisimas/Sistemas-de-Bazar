import tkinter as tk
from tkinter import ttk
import os
import csv

window = tk.Tk()
window.title("UFINDS")
window.geometry("775x519")
window.resizable(False, False)
window.iconbitmap("./assets/market.ico")

# def open_profile():
#     import profile_user
    
def exit_program():
    window.quit()


imageBackground = tk.PhotoImage(file="./assets/background.png")
iB= tk.Label(window, image=imageBackground)
iB.place(x=200,y=38, width=354)
menu = tk.Menu(window)
window.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Opções", menu=file_menu)
file_menu.add_command(label="Sair", command=exit_program)


frameRecomendacoes = tk.Frame(window, bg="#6E9C7E", width=354, height=293)
frameRecomendacoes.place(x=19, y=188)

frame3 = tk.Frame(window, bg="#6E9C7E", width=354, height=293)
frame3.place(x=390, y=188)

frame4 = tk.Frame(window, bg="#fff")

ava_label = tk.Label(window, text="AVALIAÇÃO")
ava_label.config(width=28, bg="#6E9C7E", font=28, fg="#FFf",)
ava_label.grid(row=2, column=0)
ava_label.place(x=20,y=200)


ava_label = tk.Label(window, text="Estande:")
ava_label.config(width=10, bg="#6E9C7E", font=28, fg="#FFf",)
ava_label.grid(row=6, column=0)
ava_label.place(x=25,y=253)




# tk.Label(left_frame, text="Organização:").pack()
#             tk.ttk.Combobox(left_frame, values=[i for i in range(1, 6)]).pack()

#             tk.Label(left_frame, text="Variedade:").pack()
#             tk.ttk.Combobox(left_frame, values=[i for i in range(1, 6)]).pack()

#             tk.Label(left_frame, text="Atendimento:").pack()
#             tk.ttk.Combobox(left_frame, values=[i for i in range(1, 6)]).pack()

#             tk.Label(left_frame, text="Aparência:").pack()
#             tk.ttk.Combobox(left_frame, values=[i for i in range(1, 6)]).pack()



window.mainloop()