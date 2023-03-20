import tkinter as tk


profile = tk.Tk()
profile.title("Profile")
profile.geometry("775x519")
profile.resizable(False, False)
profile.iconbitmap("./assets/market.ico")

username_label = tk.Label(profile, text="Username: {}".format(user))
username_label.pack()
password_entry = tk.Entry(profile, show="*", width=20)
password_entry.insert(0, password)
password_entry.pack()
name_entry = tk.Entry(profile, width=20)
name_entry.insert(0, name)
name_entry.pack()

def back_to_previous_screen():
     # volta para a tela anterior
    profile.destroy()

update_button = tk.Button(profile, text="Update")
update_button.pack()
back_button = tk.Button(profile, text="Back", command=back_to_previous_screen)
back_button.pack()
profile.mainloop()
    
