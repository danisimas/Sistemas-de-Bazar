import tkinter as tk
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog

class UFinds:
    def __init__(self, root):
        self.root = root
        self.root.title("UFinds - Login")
        self.root.geometry("775x519")
        self.root.resizable(0, 0)
        self.root.iconbitmap("./assets/market.ico")
        self.users = {
            "admin": "123456",
        }

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.image_login = Image.open("./assets/login.png")
        self.image_login = self.image_login.resize((114,61),Image.ANTIALIAS)
        self.image_login = ImageTk.PhotoImage(self.image_login)

        self.image_cad = Image.open("./assets/cad.png")
        self.image_cad = self.image_cad.resize((114,61),Image.ANTIALIAS)
        self.image_cad = ImageTk.PhotoImage(self.image_cad)

        self.image_cad_register = Image.open("./assets/cad.png")
        self.image_cad_register = self.image_cad_register.resize((114,61),Image.ANTIALIAS)
        self.image_cad_register = ImageTk.PhotoImage(self.image_cad_register)

        self.image_back_register = Image.open("./assets/register.png")
        self.image_back_register = self.image_back_register.resize((350, 350), Image.ANTIALIAS)
        self.image_back_register = ImageTk.PhotoImage(self.image_back_register)
        
        self.create_widgets()
        

    def background(self):
        
        self.background_image = Image.open("./assets/entrar.png")
        self.background_image = self.background_image.resize((775, 519), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0,y=0)


    def create_widgets(self):

        self.background()

        tk.Label(self.root, text="Nome:", font=20, bg="#fff").place(x=120,y=320)
        tk.Entry(self.root, textvariable=self.username).place(x=124,y=362)

        tk.Label(self.root, text="Senha:", font=28, bg="#fff").place(x=120, y=382)
        tk.Entry(self.root, textvariable=self.password, show="*").place(x=124,y=420)

        button_login = tk.Button(self.root, text="Entrar", image=self.image_login, bd=0, bg="#fff", activebackground='#FFFFFF', command=self.login)
        button_login.place(x=300, y=350)

        button_cad = tk.Button(self.root, text="Cadastrar-se", image=self.image_cad, bd=0, bg="#fff", activebackground='#FFFFFF', command=self.register)
        button_cad.place(x=300, y=430)


    def verify_register(self, register_screen, username, password, confirm_password):
    # Verificação de Cadastro
        if username.get() in self.users:
            tk.messagebox.showerror("Erro", "Nome de usuário já existe")
        elif password.get() != confirm_password.get():
            tk.messagebox.showerror("Erro", "Senhas não coincidem")
        else:
            self.users[username.get()] = password.get()
            tk.messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso")
            register_screen.destroy()
            self.root.deiconify()

    def login(self):
        if self.username.get() in self.users and self.users[self.username.get()] == self.password.get():
            self.root.destroy()
            import project
        else:
            tk.messagebox.showerror("Erro", "Nome de usuário ou senha inválidos")

    def register(self):
        register_screen = tk.Toplevel(self.root)
        register_screen.title("UFinds - Cadastro")
        register_screen.geometry("350x350")
        register_screen.resizable(False, False)
        register_screen.iconbitmap("./assets/market.ico")
        tk.Label(register_screen, image=self.image_back_register).place(x=0,y=0)

        username = tk.StringVar()
        password = tk.StringVar()
        confirm_password = tk.StringVar()

        tk.Label(register_screen, text="Nome:", font=20, bg="#fff").place(x=50,y=100)
        tk.Entry(register_screen, textvariable=username).place(x=50,y=130)

        tk.Label(register_screen, text="Senha:",font=20, bg="#fff").place(x=50,y=150)
        tk.Entry(register_screen, textvariable=password, show="*").place(x=50,y=180)

        tk.Label(register_screen, text="Confirmar Senha:",font=20, bg="#fff").place(x=50, y=200)
        tk.Entry(register_screen, textvariable=confirm_password, show="*").place(x = 50, y = 230)

        tk.Button(register_screen, text="Cadastrar", image=self.image_cad_register, bd=0, bg="#fff", activebackground="#fff", command=lambda: self.verify_register(register_screen, username, password,
         confirm_password)).place(x=70, y=280)

root = tk.Tk()
ufinds = UFinds(root)
root.mainloop()