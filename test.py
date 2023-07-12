import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("400 x 240")


def button_functions():
    print("Button pressed")


button = customtkinter.CTkButton(master=app, text="Boton prueba", command=button_functions)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
app.mainloop()
