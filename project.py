import tkinter as tk

window = tk.Tk()
window.title("UFINDS")
window.geometry("775x519")
window.resizable(False, False)
window.iconbitmap("./assets/market.ico")

imageBackground = tk.PhotoImage(file="./assets/background.png")
iB= tk.Label(window, image=imageBackground)
iB.place(x=211,y=38, width=354)

title_label = tk.Label(window, text="Avaliar estandes")
user_label = tk.Label(window, text="")
user_label.grid(row=0, column=0)

user_var = tk.StringVar()
user_entry = tk.Entry(window, textvariable=user_var)
user_entry.grid(row=0, column=1)

song_label = tk.Label(window, text="Nome da música:")
song_label.grid(row=1, column=0)

song_var = tk.StringVar()
song_entry = tk.Entry(window, textvariable=song_var)
song_entry.grid(row=1, column=1)

rating_label = tk.Label(window, text="Avaliação (1-5):")
rating_label.grid(row=2, column=0)

rating_var = tk.IntVar()
rating_entry = tk.Entry(window, textvariable=rating_var)
rating_entry.grid(row=2, column=1)

k_label = tk.Label(window, text="Número de recomendações:")
k_label.grid(row=3, column=0)

k_var = tk.IntVar()
k_entry = tk.Entry(window, textvariable=k_var)
k_entry.grid(row=3, column=1)



window.mainloop()