import tkinter as tk
from tkinter import ttk
import pandas as pd
import csv

window = tk.Tk()
window.title("UFINDS")
window.geometry("775x519")
window.resizable(True, True)
window.iconbitmap("./assets/market.ico")

file_path= "dados.csv"
coluna = "Estande"
dados = pd.read_csv("dados.csv").to_dict('records')

def dist_eucli(usuario1, usuario2):
    dist = 0
    dist = pow(usuario1['Nota_Atendimento'] - usuario2['Nota_Atendimento'], 2)
    dist += pow(usuario1['Nota_Organizacao'] - usuario2['Nota_Organizacao'], 2)
    dist += pow(usuario1['Nota_Aparencia'] - usuario2['Nota_Aparencia'], 2)
    dist += pow(usuario1['Nota_Variedade'] - usuario2['Nota_Variedade'], 2)
    return dist**0.5

def vizinho_proximo(data, resposta, k):
    vizinhos = []
    for bazar in data:
            if bazar["Estande"] != resposta['Estande']:
                vizinhos.append((bazar, dist_eucli(bazar, resposta)))
                vizinhos.sort(key=lambda tup: tup[1])
                topo = vizinhos[0:k]

    estandes = set()
    resultado = []  
    for bazar, dist in topo:
        if bazar['Estande'] not in estandes:
            resultado.append((bazar, dist))
            estandes.add(bazar['Estande'])  
    return resultado

def add_values_to_combobox(file_path, column_name, combobox):
    unique_names = set()
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row[column_name]
            if name not in unique_names:
                unique_names.add(name)
                combobox['values'] = (*combobox['values'], name)

def exit_program():
    window.quit()


imageBackground = tk.PhotoImage(file="./assets/background.png")
iB= tk.Label(window, image=imageBackground)
iB.place(x=200,y=38, width=354)

image_Button_avaliar = tk.PhotoImage(file="./assets/ava.png")


menu = tk.Menu(window)
window.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Opções", menu=file_menu)
file_menu.add_command(label="Sair", command=exit_program)


#Avaliação
frameRecomendacoes = tk.Frame(window, bg="#6E9C7E", width=354, height=293)
frameRecomendacoes.place(x=19, y=188)

#Recomendacao
frame3 = tk.Frame(window, bg="#6E9C7E", width=354, height=293)
frame3.place(x=390, y=188)

# Avaliação
ava_label = tk.Label(window, text="AVALIAÇÃO")
ava_label.config(width=28, bg="#6E9C7E", font=28, fg="#FFf",)
ava_label.grid(row=2, column=0)
ava_label.place(x=20,y=200)

# Recomendacao
ava_label_rec = tk.Label(window, text="RECOMENDAÇÃO")
ava_label_rec.config(width=28, bg="#6E9C7E", font=28, fg="#FFf",)
ava_label_rec.grid(row=2, column=0)
ava_label_rec.place(x=400,y=200)

# Estande
ava_label = tk.Label(window, text="Estande:")
ava_label.config(width=10, bg="#6E9C7E", font=20, fg="#FFf",)
ava_label.grid(row=6, column=0)
ava_label.place(x=25,y=250)
estande_frame = tk.Frame(window, bg="#6E9C7E", width=20, height=20)
estande_frame.place(x=155,y=255)
comboBox_estande = tk.ttk.Combobox(estande_frame, values=())
add_values_to_combobox(file_path,coluna,comboBox_estande)
comboBox_estande.grid(row=6, column=1)

#Atendimento
atendimento_label = tk.Label(window, text="Atendimento:")
atendimento_label.config(width=10, bg="#6E9C7E", font=20, fg="#FFf",)
atendimento_label.grid(row=6, column=0)
atendimento_label.place(x=25,y=280)
aten_frame = tk.Frame(window, bg="#6E9C7E", width=20, height=20)
aten_frame.place(x=155,y=285)
comboBox_atendimento= tk.ttk.Combobox(aten_frame, values=[i for i in range(1, 6)])
comboBox_atendimento.grid(row=6, column=1)

# Organização
org_label = tk.Label(window, text="Organização:")
org_label.config(width=10, bg="#6E9C7E", font=20, fg="#FFf",)
org_label.grid(row=6, column=0)
org_label.place(x=25,y=310)
org_frame = tk.Frame(window, bg="#6E9C7E", width=20, height=20)
org_frame.place(x=155,y=315)
comboBox_org= tk.ttk.Combobox(org_frame, values=[i for i in range(1, 6)])
comboBox_org.grid(row=6, column=1)


#Aparencia
aparencia_label = tk.Label(window, text="Aparência:")
aparencia_label.config(width=10, bg="#6E9C7E", font=20, fg="#FFf",)
aparencia_label.grid(row=6, column=0)
aparencia_label.place(x=25,y=340)
apa_frame = tk.Frame(window, bg="#6E9C7E", width=20, height=20)
apa_frame.place(x=155,y=345)
comboBox_aparencia= tk.ttk.Combobox(apa_frame, values=[i for i in range(1, 6)])
comboBox_aparencia.grid(row=6, column=1)


#Variedade
variedade_label = tk.Label(window, text="Variedade:")
variedade_label.config(width=10, bg="#6E9C7E", font=20, fg="#FFf",)
variedade_label.grid(row=6, column=0)
variedade_label.place(x=25,y=370)
va_frame = tk.Frame(window, bg="#6E9C7E", width=20, height=20)
va_frame.place(x=155,y=375)
comboBox_variedade= tk.ttk.Combobox(va_frame, values=[i for i in range(1, 6)])
comboBox_variedade.grid(row=6, column=1)



def avaliable_bazar():
    selected_estande = comboBox_estande.get()
    selected_atendimento = int(comboBox_atendimento.get())
    selected_organizacao = int(comboBox_org.get())
    selected_variedade = int(comboBox_variedade.get())
    selected_aparencia = int(comboBox_aparencia.get())

    data_comparative = {
    'Estande': selected_estande,
    'Nota_Atendimento': selected_atendimento,
    'Nota_Organizacao': selected_organizacao,
    'Nota_Aparencia': selected_aparencia,
    'Nota_Variedade': selected_variedade
    }

    knn = vizinho_proximo(dados,data_comparative,7)
    recommend_label(knn)

    comboBox_estande.set('')
    comboBox_atendimento.set('')
    comboBox_aparencia.set('')
    comboBox_org.set('')
    comboBox_variedade.set('')

def recommend_label(knn):
    count = 0
    recommend_label_list = tk.Listbox(window, bd=0, bg="#6E9C7E", font=20, fg="#fff")
    for item in knn:
        count += 1
        recommend_label_list.insert(count, item[0]["Estande"])
        recommend_label_list.config(width=28)
        recommend_label_list.grid(row=6, column=1)
        recommend_label_list.place(x=415, y=235)

button_Avaliar = tk.Button(window, image=image_Button_avaliar, bd=0, bg='#6E9C7E', activebackground='#6E9C7E', command=avaliable_bazar)
button_Avaliar.grid(row=6, column=0)
button_Avaliar.place(x=100,y=410)

window.mainloop()