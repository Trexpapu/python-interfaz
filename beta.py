import tkinter
from tkinter import ttk
import customtkinter
from PIL import Image
import os
from sqlite3 import connect
import os
import mysql.connector
#color de la interfaz 
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


#aqui agregamos las otras intefaces de las opciones

#añadir datos a un animal ya existente//////////////
def open_addAnimal_inExist(): 
    #AppMain.withdraw() #oculta la ventana principal en vez de destruirla para reinvocarla
    AppMain.destroy()
    global Add_animal_inExist_App #variable global de la ventana para destruirla en otra funcion
    Add_animal_inExist_App = customtkinter.CTk()#creamos ventana
    #agregamos esta parte para que la ventana aparezca centrada y grande sin ningun problema
    Add_animal_inExist_App.title("Agregando datos a animal existente")
    screen_width = Add_animal_inExist_App.winfo_screenwidth()
    screen_height = Add_animal_inExist_App.winfo_screenheight()
    Add_animal_inExist_App.geometry(f"{screen_width}x{screen_height}+0+0")
    buttonBack = customtkinter.CTkButton(master= Add_animal_inExist_App, text="Regresa", command=backMain1)
    buttonBack.place(relx=0.05, rely=0.05, anchor=tkinter.CENTER)



     # Agregar etiquetas y campos de entrada de texto
    animal = customtkinter.CTkLabel(master=Add_animal_inExist_App, text="Nombre del animal:")
    animal.place(relx=0.2, rely=0.2, anchor=tkinter.CENTER)
    entry_animal = customtkinter.CTkEntry(master=Add_animal_inExist_App)
    entry_animal.place(relx=0.4, rely=0.2, anchor=tkinter.CENTER)

    sintomas = customtkinter.CTkLabel(master=Add_animal_inExist_App, text="Sintomas que va a agregar:")
    sintomas.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)
    entry_sintomas = customtkinter.CTkEntry(master=Add_animal_inExist_App)
    entry_sintomas.place(relx=0.4, rely=0.3, anchor=tkinter.CENTER)

    enfermedad = customtkinter.CTkLabel(master=Add_animal_inExist_App, text="Enfermedad que va a agregar:") 
    enfermedad.place(relx=0.2, rely=0.4, anchor=tkinter.CENTER)
    entry_enfermedad = customtkinter.CTkEntry(master=Add_animal_inExist_App)
    entry_enfermedad.place(relx=0.4, rely=0.4, anchor=tkinter.CENTER)

    medicina = customtkinter.CTkLabel(master=Add_animal_inExist_App, text="Medicina que va a agregar:")
    medicina.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)
    entry_medicina = customtkinter.CTkEntry(master=Add_animal_inExist_App)
    entry_medicina.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)


    def save_data():
        # Obtener los valores ingresados en los campos de entrada de texto
        animalSQL = entry_animal.get().lower()
        sintomasSQL = entry_sintomas.get().lower()
        enfermedadSQL = entry_enfermedad.get().lower() 
        medicinaSQL = entry_medicina.get().lower() 
        if animalSQL and sintomasSQL and enfermedadSQL and medicinaSQL:

            nombre_animal= animalSQL
            # Realizar la consulta para obtener el ID del animal por su nombre
            query = "SELECT ID_animal FROM animales WHERE Animal = %s"
            mycursor.execute(query, (nombre_animal,))
            result = mycursor.fetchone()
            if result:
                id_animal=result[0]
                sintomas = sintomasSQL
                enfermedad = enfermedadSQL
                medicina = medicinaSQL
                mycursor.execute("INSERT INTO medicinas(Medicina) VALUES(%s)", (medicina,))
                id_medicina = mycursor.lastrowid
                mycursor.execute("INSERT INTO enfermedades(Enfermedad, ID_medicina) VALUES(%s, %s)", (enfermedad, id_medicina))
                id_enfermedad = mycursor.lastrowid
                mycursor.execute("INSERT INTO sintomas(Sintomas, ID_animal, ID_enfermedad) VALUES(%s, %s, %s)", (sintomas, id_animal, id_enfermedad))
                # Confirmar los cambios realizados en la base de datos
                mydbd.commit()
                info = customtkinter.CTkLabel(master=Add_animal_inExist_App, text="Datos enviados correctamente")
                info.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
                Add_animal_inExist_App.after(2000, lambda: info.destroy())
                
                

                

            else:
                info = customtkinter.CTkLabel(master=Add_animal_inExist_App, text="Error no existe un animal con ese nombre")
                info.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
                Add_animal_inExist_App.after(2000, lambda: info.destroy())
        else:
            info = customtkinter.CTkLabel(master=Add_animal_inExist_App, text="Error no a llenado todos los campos")
            info.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
            Add_animal_inExist_App.after(2000, lambda: info.destroy())
           
            



    buttonGuardar = customtkinter.CTkButton(master=Add_animal_inExist_App, text="Guardar",fg_color="green", command=save_data)
    buttonGuardar.place(relx=0.6, rely=0.6, anchor=tkinter.CENTER)

    Add_animal_inExist_App.mainloop()


    #añadir datos a un animal ya existente////////////////////////////


#añadir animal///////////////////////////

def open_addAnimal():
    AppMain.destroy()
    global Add_animal_App
    Add_animal_App = customtkinter.CTk()
    Add_animal_App.title("Agregando datos de animal")
    screen_width = Add_animal_App.winfo_screenwidth()
    screen_height = Add_animal_App.winfo_screenheight()
    Add_animal_App.geometry(f"{screen_width}x{screen_height}+0+0")
    buttonBack = customtkinter.CTkButton(master=Add_animal_App, text="Regresa", command=backMain2)
    buttonBack.place(relx=0.05, rely=0.05, anchor=tkinter.CENTER)

    #backend de añadir animal
    # Agregar etiquetas y campos de entrada de texto
    animal = customtkinter.CTkLabel(master=Add_animal_App, text="Animal que va a agregar:")
    animal.place(relx=0.2, rely=0.2, anchor=tkinter.CENTER)
    entry_animal = customtkinter.CTkEntry(master=Add_animal_App)
    entry_animal.place(relx=0.4, rely=0.2, anchor=tkinter.CENTER)

    sintomas = customtkinter.CTkLabel(master=Add_animal_App, text="Sintomas que va a agregar:")
    sintomas.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)
    entry_sintomas = customtkinter.CTkEntry(master=Add_animal_App)
    entry_sintomas.place(relx=0.4, rely=0.3, anchor=tkinter.CENTER)

    enfermedad = customtkinter.CTkLabel(master=Add_animal_App, text="Enfermedad que va a agregar:") 
    enfermedad.place(relx=0.2, rely=0.4, anchor=tkinter.CENTER)
    entry_enfermedad = customtkinter.CTkEntry(master=Add_animal_App)
    entry_enfermedad.place(relx=0.4, rely=0.4, anchor=tkinter.CENTER)

    medicina = customtkinter.CTkLabel(master=Add_animal_App, text="Medicina que va a agregar:")
    medicina.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)
    entry_medicina = customtkinter.CTkEntry(master=Add_animal_App)
    entry_medicina.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)


    def save_data():
        #backend
        # Obtener los valores ingresados en los campos de entrada de texto
        animalSQL = entry_animal.get().lower()
        sintomasSQL = entry_sintomas.get().lower()
        enfermedadSQL = entry_enfermedad.get().lower()
        medicinaSQL = entry_medicina.get().lower()
        if animalSQL and sintomasSQL and enfermedadSQL and medicinaSQL:
            # Hacer algo con los datos guardados en las variables (por ejemplo, imprimirlos)
            #sql para añadir al animal
            try:

                animal = animalSQL
        
                # Realizar la consulta para verificar si ya existe un animal con ese nombre
                query = "SELECT ID_animal FROM animales WHERE Animal = %s"
                mycursor.execute(query, (animal,))
                
                # Obtener el resultado de la consulta
                result = mycursor.fetchone()
                
                if result:
                    info = customtkinter.CTkLabel(master=Add_animal_App, text="Error ya existe un animal con ese nombre")
                    info.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
                    Add_animal_App.after(2000, lambda: info.destroy())

                    
                else:
                    sintomas = sintomasSQL
                    enfermedad = enfermedadSQL
                    medicina = medicinaSQL
                    
                    # Insertar el nuevo animal en la base de datos
                    mycursor.execute("INSERT INTO animales(Animal) VALUES(%s)", (animal,))
                    id_animal = mycursor.lastrowid
                    
                    mycursor.execute("INSERT INTO medicinas(Medicina) VALUES(%s)", (medicina,))
                    id_medicina = mycursor.lastrowid
                    
                    mycursor.execute("INSERT INTO enfermedades(Enfermedad, ID_medicina) VALUES(%s, %s)", (enfermedad, id_medicina))
                    id_enfermedad = mycursor.lastrowid
                    
                    mycursor.execute("INSERT INTO sintomas(Sintomas, ID_animal, ID_enfermedad) VALUES(%s, %s, %s)", (sintomas, id_animal, id_enfermedad))
                    
                    # Confirmar los cambios realizados en la base de datos
                    mydbd.commit()
                    info = customtkinter.CTkLabel(master=Add_animal_App, text="Datos enviados correctamente")
                    info.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
                    Add_animal_App.after(2000, lambda: info.destroy())
                    

            except mysql.connector.IntegrityError:

                info = customtkinter.CTkLabel(master=Add_animal_App, text="Error ya existe un animal con ese nombre")
                info.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
                Add_animal_App.after(2000, lambda: info.destroy())
                
        

            
            
            
        else:
            info = customtkinter.CTkLabel(master=Add_animal_App, text="Error no a llenado todos los campos")
            info.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
            Add_animal_App.after(2000, lambda: info.destroy())
            
            
            
            

    buttonGuardar = customtkinter.CTkButton(master=Add_animal_App, text="Guardar",fg_color="green", command=save_data)
    buttonGuardar.place(relx=0.6, rely=0.6, anchor=tkinter.CENTER)

    


    Add_animal_App.mainloop()


#añadir animal //////////////////////

def openAskAnimalsAndSicks():
    AppMain.destroy()
    global Ask_animals_and_sicks_App
    Ask_animals_and_sicks_App = customtkinter.CTk()
    Ask_animals_and_sicks_App.title("Buscar animal y enfermedad")
    screen_width = Ask_animals_and_sicks_App.winfo_screenwidth()
    screen_height = Ask_animals_and_sicks_App.winfo_screenheight()
    Ask_animals_and_sicks_App.geometry(f"{screen_width}x{screen_height}+0+0")
    buttonBack = customtkinter.CTkButton(master=Ask_animals_and_sicks_App, text="Regresa", command=backMain3)
    buttonBack.place(relx=0.05, rely=0.05, anchor=tkinter.CENTER)
    animal = customtkinter.CTkLabel(master=Ask_animals_and_sicks_App, text="Animal que busca:")
    animal.place(relx=0.2, rely=0.2, anchor=tkinter.CENTER)
    entry_animal = customtkinter.CTkEntry(master=Ask_animals_and_sicks_App)
    entry_animal.place(relx=0.4, rely=0.2, anchor=tkinter.CENTER)
    enfermedad = customtkinter.CTkLabel(master=Ask_animals_and_sicks_App, text="Enfermedad del animal: ")
    enfermedad.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)
    entry_enfermedad = customtkinter.CTkEntry(master=Ask_animals_and_sicks_App)
    entry_enfermedad.place(relx=0.4, rely=0.3, anchor=tkinter.CENTER)



    def showTable(id_animal, id_enfermedad):
        Ask_animals_and_sicks_App.destroy()
        global show_table_app
        show_table_app = tkinter.Tk()
        show_table_app.title("Información especifica")
        show_table_app.configure(background="#6C737E")  # Cambiar el fondo de la ventana

        screen_width = show_table_app.winfo_screenwidth()
        screen_height = show_table_app.winfo_screenheight()
        show_table_app.geometry(f"{screen_width}x{screen_height}+200+0")
        buttonBack = tkinter.Button(master=show_table_app, text="Regresa", command=backToSicksAndAnimal)
        buttonBack.place(relx=0.05, rely=0.05, anchor=tkinter.CENTER)

        # Configurar estilo personalizado
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#000000", foreground="#ffffff", fieldbackground="#1f497d")
        style.configure("Custom.Treeview.Heading", background="#000000", foreground="#ffffff", font=("Arial", 10, "bold"))

        # Cambiar el estilo predeterminado de ttk
        style.theme_use("default")  # Puedes probar diferentes estilos (clam, alt, default, etc.)

        table = ttk.Treeview(show_table_app, columns=("Animales", "Sintomas", "Enfermedades", "Medicinas"), style="Custom.Treeview")

        # Configurar encabezados de columna
        table.heading("Animales", text="Animales", anchor="center")
        table.heading("Sintomas", text="Sintomas", anchor="center")
        table.heading("Enfermedades", text="Enfermedades", anchor="center")
        table.heading("Medicinas", text="Medicinas", anchor="center")

        # Configurar alineación de las columnas
        table.column("Animales", anchor="center")  # Alineación al centro
        table.column("Sintomas", anchor="center")  # Alineación al centro
        table.column("Enfermedades", anchor="center")  # Alineación al centro
        table.column("Medicinas", anchor="center")  # Alineación al centro

        # Agregar datos a la tabla
        query = """
                    SELECT a.Animal, s.Sintomas, e.Enfermedad, m.Medicina
                    FROM animales AS a
                    JOIN sintomas AS s ON a.ID_animal = s.ID_animal
                    JOIN enfermedades AS e ON s.ID_enfermedad = e.ID_enfermedad
                    JOIN medicinas AS m ON e.ID_medicina = m.ID_medicina
                    WHERE a.ID_animal = %s and s.ID_enfermedad= %s
                """
        mycursor.execute(query, (id_animal, id_enfermedad))
        for i in mycursor:
            table.insert("", 0, values=i)

        # Aplicar estilo personalizado a la tabla
        table.configure(style="Custom.Treeview")

        table.pack()

        show_table_app.mainloop()


    def search():
        animalSearchSQL = entry_animal.get()
        enfermedadSearchSQL = entry_enfermedad.get()
        if enfermedadSearchSQL and animalSearchSQL:
            nombre_animal = animalSearchSQL

            # Realizar la consulta para obtener el ID del animal por su nombre
            query = "SELECT ID_animal FROM animales WHERE Animal = %s"
            mycursor.execute(query, (nombre_animal,))
            result1 = mycursor.fetchone()


            nombre_enfermedad = enfermedadSearchSQL

            # Realizar la consulta para obtener el ID del animal por su nombre
            query = "SELECT ID_enfermedad FROM enfermedades WHERE enfermedad = %s"
            mycursor.execute(query, (nombre_enfermedad,))
            result2 = mycursor.fetchone()


            if result1 and result2:
                id_animal = result1[0]
                id_enfermedad = result2[0]
                showTable(id_animal, id_enfermedad)
                
                
            else:
                info = customtkinter.CTkLabel(master=Ask_animals_and_sicks_App, text="Error no existe un animal o enfermedad con esos nombres")
                info.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
                Ask_animals_and_sicks_App.after(2000, lambda: info.destroy())
               
            
            
            
        else:
            info = customtkinter.CTkLabel(master=Ask_animals_and_sicks_App, text="Error no a llenado todos los campos")
            info.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
            Ask_animals_and_sicks_App.after(2000, lambda: info.destroy())

        


    botonBuscar = customtkinter.CTkButton(master=Ask_animals_and_sicks_App, text="Buscar",fg_color="green", command=search)
    botonBuscar.place(relx=0.6, rely=0.6, anchor=tkinter.CENTER)




    Ask_animals_and_sicks_App.mainloop()

def openAskAllAnimals():
    AppMain.destroy()
    global Ask_all_animals_App
    Ask_all_animals_App = tkinter.Tk()
    Ask_all_animals_App.title("Informacion general")
    Ask_all_animals_App.configure(background="#6C737E")  # Cambiar el fondo de la ventana

    screen_width = Ask_all_animals_App.winfo_screenwidth()
    screen_height = Ask_all_animals_App.winfo_screenheight()
    Ask_all_animals_App.geometry(f"{screen_width}x{screen_height}+200+0")
    buttonBack = tkinter.Button(master=Ask_all_animals_App, text="Regresa", command=backMain4)
    buttonBack.place(relx=0.05, rely=0.05, anchor=tkinter.CENTER)

    # Configurar estilo personalizado
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#000000", foreground="#ffffff", fieldbackground="#1f497d")
    style.configure("Custom.Treeview.Heading", background="#000000", foreground="#ffffff", font=("Arial", 10, "bold"))

    # Cambiar el estilo predeterminado de ttk
    style.theme_use("default")  # Puedes probar diferentes estilos (clam, alt, default, etc.)

    table = ttk.Treeview(Ask_all_animals_App, columns=("Animales", "Sintomas", "Enfermedades", "Medicinas"), style="Custom.Treeview")

    # Configurar encabezados de columna
    table.heading("Animales", text="Animales", anchor="center")
    table.heading("Sintomas", text="Sintomas", anchor="center")
    table.heading("Enfermedades", text="Enfermedades", anchor="center")
    table.heading("Medicinas", text="Medicinas", anchor="center")

    # Configurar alineación de las columnas
    table.column("Animales", anchor="center")  # Alineación al centro
    table.column("Sintomas", anchor="center")  # Alineación al centro
    table.column("Enfermedades", anchor="center")  # Alineación al centro
    table.column("Medicinas", anchor="center")  # Alineación al centro

    # Agregar datos a la tabla
    mycursor.execute("SELECT a.Animal, s.Sintomas, e.Enfermedad, m.Medicina FROM animales AS a JOIN sintomas AS s ON  a.ID_animal = s.ID_animal JOIN enfermedades AS e ON s.ID_enfermedad = e.ID_enfermedad JOIN medicinas AS m ON m.ID_medicina = e.ID_medicina ORDER BY a.Animal ASC")
    for i in mycursor:
        table.insert("", 0, values=i)

    # Aplicar estilo personalizado a la tabla
    table.configure(style="Custom.Treeview")

    table.pack()

    Ask_all_animals_App.mainloop()



def editData():
    
    def doubleClickTable(event):
        claveVieja = str(table.item(table.selection())["values"][0])

        nuevoAnimal = (0,str(table.item(table.selection())["text"]))
        print(nuevoAnimal)

       
    AppMain.destroy()
    global edit_data_App
    edit_data_App = tkinter.Tk()
    edit_data_App.title("Modificando datos")
    screen_width = edit_data_App.winfo_screenwidth()
    screen_height = edit_data_App.winfo_screenheight()
    edit_data_App.geometry(f"{screen_width}x{screen_height}+200+0")
    buttonBack = tkinter.Button(master=edit_data_App, text="Regresa", command=backMain5)
    buttonBack.place(relx=0.05, rely=0.05, anchor=tkinter.CENTER)

     # Configurar estilo personalizado
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#000000", foreground="#ffffff", fieldbackground="#1f497d")
    style.configure("Custom.Treeview.Heading", background="#000000", foreground="#ffffff", font=("Arial", 10, "bold"))

    # Cambiar el estilo predeterminado de ttk
    style.theme_use("default")  # Puedes probar diferentes estilos (clam, alt, default, etc.)

    table = ttk.Treeview(edit_data_App, columns=("Animales", "Sintomas", "Enfermedades", "Medicinas", "Doble click para modificar"), style="Custom.Treeview")
    

    # Configurar encabezados de columna
    table.bind("<Double-Button-1>", doubleClickTable)
    table.heading("Animales", text="Animales", anchor="center")
    table.heading("Sintomas", text="Sintomas", anchor="center")
    table.heading("Enfermedades", text="Enfermedades", anchor="center")
    table.heading("Medicinas", text="Medicinas", anchor="center")
    table.heading("Doble click para modificar", text="Doble click para modificar", anchor="center")
    

    # Configurar alineación de las columnas
    table.column("Animales", anchor="center")  # Alineación al centro
    table.column("Sintomas", anchor="center")  # Alineación al centro
    table.column("Enfermedades", anchor="center")  # Alineación al centro
    table.column("Medicinas", anchor="center")  # Alineación al centro
    

    # Agregar datos a la tabla
    
    mycursor.execute("SELECT a.Animal, s.Sintomas, e.Enfermedad, m.Medicina FROM animales AS a JOIN sintomas AS s ON  a.ID_animal = s.ID_animal JOIN enfermedades AS e ON s.ID_enfermedad = e.ID_enfermedad JOIN medicinas AS m ON m.ID_medicina = e.ID_medicina ORDER BY a.Animal ASC")
    for i in mycursor:
        table.insert("", 0, values=i)
       

    # Aplicar estilo personalizado a la tabla
    table.configure(style="Custom.Treeview")

    table.pack()

    edit_data_App.mainloop()

def deleteDataF():
    AppMain.destroy()
    global delete_data_App
    delete_data_App = customtkinter.CTk()
    delete_data_App.title("Borrando datos")
    screen_width = delete_data_App.winfo_screenwidth()
    screen_height = delete_data_App.winfo_screenheight()
    delete_data_App.geometry(f"{screen_width}x{screen_height}+0+0")
    buttonBack = customtkinter.CTkButton(master=delete_data_App, text="Regresa", command=backMain6)
    buttonBack.place(relx=0.05, rely=0.05, anchor=tkinter.CENTER)
    delete_data_App.mainloop()








#aqui van todos los backmains
def backMain1(): 
   Add_animal_inExist_App.destroy()#destruimos ventana
   #AppMain.deiconify()#vuelve a abrir la ventana indicada
   Main()
def backMain2():
    Add_animal_App.destroy()
    Main()
def backMain3():
    Ask_animals_and_sicks_App.destroy()
    Main()
def backMain4():
    Ask_all_animals_App.destroy()
    Main()
def backMain5():
    edit_data_App.destroy()
    Main()
def backMain6():
    delete_data_App.destroy()
    Main()
def backToSicksAndAnimal():
    show_table_app.destroy()
    Main()

    



def Main():
    #interfaz principal

    #cargamos las imagenes
    AddImage = customtkinter.CTkImage(dark_image=Image.open(os.path.join("add_user_dark.png")), size=(20, 20))
    AskImage = customtkinter.CTkImage(dark_image=Image.open(os.path.join("chat_dark.png")), size=(20, 20))
    EditImage = customtkinter.CTkImage(dark_image=Image.open(os.path.join("edit.png")), size=(20,20))
    DeleteImage = customtkinter.CTkImage(dark_image=Image.open(os.path.join("delete.jpg")), size=(20,20))

    global AppMain
    AppMain = customtkinter.CTk()
    AppMain.title("Menu de opciones")
    #agregamos esta parte para que la ventana aparezca centrada y grande sin ningun problema
    screen_width = AppMain.winfo_screenwidth()
    screen_height = AppMain.winfo_screenheight()
    AppMain.geometry(f"{screen_width}x{screen_height}+0+0")

    AddAnimal = customtkinter.CTkButton(master= AppMain, text="Añadir animal, sintomas, enfermedad y medicina",fg_color="purple",image=AddImage, command=open_addAnimal)
    AddAnimal.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)

    AddDatesOfAnimal = customtkinter.CTkButton(master= AppMain, text="Añadir datos a un animal ya existente", fg_color="purple",image=AddImage, command=open_addAnimal_inExist)
    AddDatesOfAnimal.place(relx=0.1, rely=0.3, anchor=tkinter.CENTER)


    askAnimalsAndSicks = customtkinter.CTkButton(master= AppMain, text="Ver animales y enfermedad", fg_color="green", image=AskImage, command=openAskAnimalsAndSicks)
    askAnimalsAndSicks.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)

    askAllAnimals = customtkinter.CTkButton(master= AppMain, text="Ver todos los datos", fg_color="green", image=AskImage, command=openAskAllAnimals)
    askAllAnimals.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)

    modifyData = customtkinter.CTkButton(master= AppMain, text = "Modificar datos", fg_color="royalblue", image=EditImage, command=editData)
    modifyData.place(relx=0.45, rely=0.2, anchor=tkinter.CENTER)

    deleteData = customtkinter.CTkButton(master= AppMain, text = "Borrar datos", fg_color="red", image=DeleteImage, command= deleteDataF)
    deleteData.place(relx=0.45, rely=0.3, anchor=tkinter.CENTER)
    
    #imagen de fondo 
    bg_image = customtkinter.CTkImage(Image.open( "logo1.png"),
                                               size=(500, 400))
    bg_image_label = customtkinter.CTkLabel(image=bg_image, master=AppMain, text="")
    bg_image_label.place(relx=0.6, rely=0.2)
    AppMain.mainloop()


#parte de conexion a sql
mydbd= mysql.connector.connect(host="127.0.0.1", user="root", password="aPERRITOMAN12", database="mascotas")
mycursor= mydbd.cursor()
print("Conexion exitosa :D")


Main()