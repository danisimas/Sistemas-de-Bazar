

import tkinter as tk
from tkinter import messagebox

# Conjunto de dados de exemplo
data = [
    {"user": "Alice", "song": "A", "rating": 5},
    {"user": "Bob", "song": "A", "rating": 3},
    {"user": "Charlie", "song": "A", "rating": 4},
    {"user": "Alice", "song": "B", "rating": 4},
    {"user": "Bob", "song": "B", "rating": 5},
    {"user": "Charlie", "song": "B", "rating": 3},
    {"user": "Alice", "song": "C", "rating": 2},
    {"user": "Bob", "song": "C", "rating": 2},
    {"user": "Charlie", "song": "C", "rating": 1},
    {"user": "Charlie", "song": "D", "rating": 5}
]

# Função para recomendar música para um usuário baseado na média das avaliações
def recommend_song(user, k):
    songs = {}
    for d in data:
        if d["user"] != user:
            if d["song"] not in songs:
                songs[d["song"]] = {"rating": 0, "votes": 0}
            songs[d["song"]]["rating"]  += d["rating"]
            songs[d["song"]]["votes"]  += 1
    for song in songs:
        songs[song]["rating"] = songs[song]["rating"] / songs[song]["votes"]
    rec_songs = []
    for song in songs:
        if songs[song]["rating"] >= 4:
            rec_songs.append(song)
    return rec_songs[:k]

def submit_rating():
    song = song_var.get()
    rating = rating_var.get()
    user = user_var.get()
    data.append({"user": user, "song": song, "rating": rating})
    messagebox.showinfo("Sucesso", f"Avaliação da música {song} foi adicionada com sucesso")
    
def recommend():
    user = user_var.get()
    k = k_var.get()
    rec_songs = recommend_song(user, k)
    messagebox.showinfo("Recomendações", f"As {k} músicas recomendadas para o usuário {user} são: {rec_songs}")


root = tk.Tk()
root.title("Sistema de Recomendação de Música")

user_label = tk.Label(root, text="Nome do usuário:")
user_label.grid(row=0, column=0)

user_var = tk.StringVar()
user_entry = tk.Entry(root, textvariable=user_var)
user_entry.grid(row=0, column=1)

song_label = tk.Label(root, text="Nome da música:")
song_label.grid(row=1, column=0)

song_var = tk.StringVar()
song_entry = tk.Entry(root, textvariable=song_var)
song_entry.grid(row=1, column=1)

rating_label = tk.Label(root, text="Avaliação (1-5):")
rating_label.grid(row=2, column=0)

rating_var = tk.IntVar()
rating_entry = tk.Entry(root, textvariable=rating_var)
rating_entry.grid(row=2, column=1)

k_label = tk.Label(root, text="Número de recomendações:")
k_label.grid(row=3, column=0)

k_var = tk.IntVar()
k_entry = tk.Entry(root, textvariable=k_var)
k_entry.grid(row=3, column=1)

submit_button = tk.Button(root, text="Enviar avaliação", command=submit_rating)
submit_button.grid(row=4, column=0)

recommend_button = tk.Button(root, text="Recomendar músicas", command=recommend)
recommend_button.grid(row=4, column=1)

root.mainloop()
