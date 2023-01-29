import customtkinter
import os
from PIL import Image
#import tkinter

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("775x519")
app.resizable(False, False)
app.title("UFINDS - Logado")
app.after(201, lambda :app.iconbitmap('./assets/market.ico'))




app.mainloop()
