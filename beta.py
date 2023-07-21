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




#añadir animal///////////////////////////

def open_addAnimal():
    connect()
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
                    info = customtkinter.CTkLabel(master=Add_animal_App, text="Datos enviados correctamente")
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
                    # Cerrar el cursor después de usarlo y conexion
                    
                    

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
    connect()
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
       
        mycursor.close()
        mydbd.close()
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

                query = """
                    SELECT a.Animal, s.Sintomas, e.Enfermedad, m.Medicina
                    FROM animales AS a
                    JOIN sintomas AS s ON a.ID_animal = s.ID_animal
                    JOIN enfermedades AS e ON s.ID_enfermedad = e.ID_enfermedad
                    JOIN medicinas AS m ON e.ID_medicina = m.ID_medicina
                    WHERE a.ID_animal = %s and s.ID_enfermedad= %s
                """
                
                mycursor.execute(query, (id_animal, id_enfermedad))
                results = mycursor.fetchall()
                if results:
                    showTable(id_animal, id_enfermedad)
                    
                else:
                    info = customtkinter.CTkLabel(master=Ask_animals_and_sicks_App, text="Error no existe un animal o enfermedad con esos nombres")
                    info.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
                    Ask_animals_and_sicks_App.after(2000, lambda: info.destroy())
                            
                
                
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
    connect()
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
    mycursor.close()
    mydbd.close()

    # Aplicar estilo personalizado a la tabla
    table.configure(style="Custom.Treeview")

    table.pack()

    Ask_all_animals_App.mainloop()



def editData(): 
    connect()
    def doubleClickTable(event): #funcion abre otra ventana para borrar o editar
        def backToTable():
            selectDataApp.destroy()
        def updateData():

            #obteniendo todos los ID de los valores de la tabla
            query0 = "SELECT ID_animal FROM animales WHERE Animal = %s"
            mycursor.execute(query0,(animal_t,))
            id_animal_t = mycursor.fetchone()
            id_animal_t = id_animal_t[0] #extraer valor de la tupla
            query1= "SELECT ID_sintomas FROM sintomas WHERE Sintomas = %s"
            mycursor.execute(query1,(sintomas_t,))
            id_sintomas_t=mycursor.fetchone()
            query3="SELECT ID_enfermedad FROM enfermedades WHERE Enfermedad = %s"
            mycursor.execute(query3,(enfermedades_t,))
            id_enfermedad_t = mycursor.fetchone()
            query4="SELECT ID_medicina FROM medicinas WHERE Medicina = %s"
            mycursor.execute(query4,(medicinas_t,))
            id_medicina_t=mycursor.fetchone()

            #obteniendo los datos de los entry y pasandolos a minusculas
            animalSQL_t = entry_animal.get().lower()
            sintomasSQL_t = entry_sintomas.get().lower()
            enfermedadesSQL_t = entry_enfermedad.get().lower()
            medicinasSQL_t = entry_medicina.get().lower()
            if animalSQL_t and sintomasSQL_t and enfermedadesSQL_t and medicinasSQL_t:
                #Viendo si cambio el nombre del animal o no

                query5="SELECT ID_animal FROM animales WHERE Animal = %s"
                mycursor.execute(query5, (animalSQL_t, ))
                result = mycursor.fetchone()
                if result: #si ya existe un animal con ese nombre hacemos el update
                    #hacemos los update sin problemas debido a que el nombre del animal no cambia
                    queryUpdateAnimal = "SELECT ID_animal FROM animales WHERE Animal = %s"
                    mycursor.execute(queryUpdateAnimal, (animalSQL_t, )) 
                    ID_update_animal = mycursor.fetchone()
                    ID_update_animal = ID_update_animal[0] #extraer valor de la tupla
                    id_sintomas_t = id_sintomas_t[0] #extaer valor de tupla

                    #update nombre animal (en caso de que necesite redireccionar a otro ya existente)
                    queryn = "UPDATE sintomas SET ID_animal = %s WHERE ID_sintomas = %s"
                    mycursor.execute(queryn, (ID_update_animal, id_sintomas_t))

                    query6 = "UPDATE sintomas SET Sintomas = %s WHERE ID_sintomas = %s"
                    
                    mycursor.execute(query6,(sintomasSQL_t, id_sintomas_t))

                    query7 = "UPDATE enfermedades SET Enfermedad = %s WHERE ID_enfermedad = %s"
                    id_enfermedad_t = id_enfermedad_t[0]  # Extraer el valor de la tupla
                    mycursor.execute(query7, (enfermedadesSQL_t, id_enfermedad_t))
                    query8 = "UPDATE medicinas SET Medicina = %s WHERE ID_medicina = %s"
                    id_medicina_t = id_medicina_t[0]  # Extraer el valor de la tupla
                    mycursor.execute(query8, (medicinasSQL_t, id_medicina_t))
                    mydbd.commit()
                    info = customtkinter.CTkLabel(master=selectDataApp, text="Datos actualizados correctamente")
                    info.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
                    selectDataApp.after(2000, lambda: info.destroy())
                    mycursor.close()
                    mydbd.close()
                    #llamamos a la funcion update table despues de dos segundos
                    selectDataApp.after(2000, lambda: updateTable())
                    
                else:#si hace modificacion del nombre por un animal que no exista en la tabla hacemos delete e instertamos nuevos miembros
                    #tenemos que hacer el delete de los datos que fueron seleccionar y generar un nuevo miembro en la tabla
                    query9 = "DELETE FROM sintomas WHERE ID_sintomas = %s"
                    id_sintomas_t = id_sintomas_t[0]
                    mycursor.execute(query9, (id_sintomas_t, ))
                    query10 = "DELETE FROM enfermedades WHERE ID_enfermedad = %s"
                    id_enfermedad_t = id_enfermedad_t[0]  # Extraer el valor de la tupla
                    mycursor.execute(query10, (id_enfermedad_t, ))
                    query11 = "DELETE FROM medicinas WHERE ID_medicina = %s"
                    id_medicina_t = id_medicina_t[0]  # Extraer el valor de la tupla
                    mycursor.execute(query11, (id_medicina_t, ))

                    animal = animalSQL_t
                    sintomas = sintomasSQL_t
                    enfermedad = enfermedadesSQL_t
                    medicina = medicinasSQL_t
                    
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
                    info = customtkinter.CTkLabel(master=selectDataApp, text="Datos actualizados correctamente")
                    info.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
                    selectDataApp.after(2000, lambda: info.destroy())
                    mycursor.close()
                    mydbd.close()
                    #llamamos a la funcion update table despues de dos segundos
                    selectDataApp.after(2000, lambda: updateTable()) 
            else:
                info = customtkinter.CTkLabel(master=selectDataApp, text="Error no a llenado todos los campos")
                info.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
                selectDataApp.after(2000, lambda: info.destroy())
            
        def deleteData():

            #obteniendo todos los ID de los valores de la tabla para borrar solo lo seleccionado sin importar si modifica en los entry
            query0 = "SELECT ID_animal FROM animales WHERE Animal = %s"
            mycursor.execute(query0,(animal_t,))
            id_animal_t = mycursor.fetchone()
            id_animal_t = id_animal_t[0] #extraer valor de la tupla
            query1= "SELECT ID_sintomas FROM sintomas WHERE Sintomas = %s AND ID_animal = %s"
            mycursor.execute(query1,(sintomas_t, id_animal_t))
            id_sintomas_t=mycursor.fetchone()
            query3="SELECT ID_enfermedad FROM sintomas WHERE Sintomas = %s AND ID_animal = %s"
            mycursor.execute(query3,(sintomas_t, id_animal_t))
            id_enfermedad_t = mycursor.fetchone()
            id_enfermedad_t = id_enfermedad_t[0]  # Extraer el valor de la tupla
            #prueba de delete buscando el id_medicina desde tabla enfermedades
            query4="SELECT ID_medicina FROM enfermedades WHERE ID_enfermedad = %s"
            mycursor.execute(query4,(id_enfermedad_t,))
            id_medicina_t=mycursor.fetchone()
            

            
            #pendiente realizar pruebas de deletes cuando hay sintomas con el mismo texto, revisar porque noo se puede realizar el delete del update
            id_sintomas_t = id_sintomas_t[0] #extraer el valor de la tupla
            
            id_medicina_t = id_medicina_t[0]  # Extraer el valor de la tupla
            

            #haciendo los deletes
            query9 = "DELETE FROM sintomas WHERE ID_sintomas = %s AND ID_animal = %s"
            mycursor.execute(query9, (id_sintomas_t, id_animal_t)) 
            query10 = "DELETE FROM enfermedades WHERE ID_enfermedad = %s AND ID_medicina = %s"
            
            mycursor.execute(query10, (id_enfermedad_t, id_medicina_t))
            query11 = "DELETE FROM medicinas WHERE ID_medicina = %s"
            mycursor.execute(query11, (id_medicina_t, ))

            
            # Confirmar los cambios realizados en la base de datos
            mydbd.commit()
            info = customtkinter.CTkLabel(master=selectDataApp, text="Datos borrados correctamente")
            info.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)
            selectDataApp.after(2000, lambda: info.destroy())
            #viendo si ya no existe el nombre del animal para borrarlo completamente PENDIENTE
            mycursor.close()
            mydbd.close()
            #llamamos a la funcion update table despues de dos segundos
            selectDataApp.after(2000, lambda: updateTable())

        
        
        # Obtener todos los valores de la fila seleccionada
        valoresFila = table.item(table.selection())["values"]
        
        
        # Acceder a valores individuales de la fila seleccionada
        global animal_t
        global sintomas_t
        global enfermedades_t
        global medicinas_t
        animal_t = valoresFila[0]
        sintomas_t = valoresFila[1]
        enfermedades_t = valoresFila[2]
        medicinas_t = valoresFila[3]

        global selectDataApp
        selectDataApp = customtkinter.CTk()
        selectDataApp.title("Modificando datos")
        screen_width = selectDataApp.winfo_screenwidth()
        screen_height = selectDataApp.winfo_screenheight()
        selectDataApp.geometry(f"{screen_width}x{screen_height}+0+0")
        buttonBack = customtkinter.CTkButton(master=selectDataApp, text="Regresa", command=backToTable)
        buttonBack.place(relx=0.05, rely=0.05, anchor=tkinter.CENTER)
        # Agregar etiquetas y campos de entrada de texto
        animal = customtkinter.CTkLabel(master=selectDataApp, text="Animal:")
        animal.place(relx=0.2, rely=0.2, anchor=tkinter.CENTER)
        entry_animal = customtkinter.CTkEntry(master=selectDataApp)
        entry_animal.place(relx=0.4, rely=0.2, anchor=tkinter.CENTER)

        sintomas = customtkinter.CTkLabel(master=selectDataApp, text="Sintomas:")
        sintomas.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)
        entry_sintomas = customtkinter.CTkEntry(master=selectDataApp)
        entry_sintomas.place(relx=0.4, rely=0.3, anchor=tkinter.CENTER)

        enfermedad = customtkinter.CTkLabel(master=selectDataApp, text="Enfermedad:") 
        enfermedad.place(relx=0.2, rely=0.4, anchor=tkinter.CENTER)
        entry_enfermedad = customtkinter.CTkEntry(master=selectDataApp)
        entry_enfermedad.place(relx=0.4, rely=0.4, anchor=tkinter.CENTER)

        medicina = customtkinter.CTkLabel(master=selectDataApp, text="Medicina:")
        medicina.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)
        entry_medicina = customtkinter.CTkEntry(master=selectDataApp)
        entry_medicina.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)
        entry_animal.insert(0, animal_t)
        entry_enfermedad.insert(0, enfermedades_t)
        entry_sintomas.insert(0, sintomas_t)
        entry_medicina.insert(0, medicinas_t)

        #pendiente agregar fotos a los botones
        modifyButton = customtkinter.CTkButton(master=selectDataApp, text="Actualizar",fg_color="green", command=updateData)
        modifyButton.place(relx=0.6, rely=0.6, anchor=tkinter.CENTER)
        deleteButton = customtkinter.CTkButton(master=selectDataApp, text="Borrar", fg_color="red", command=deleteData)
        deleteButton.place(relx=0.7, rely=0.6, anchor=tkinter.CENTER)
        

        selectDataApp.mainloop()

       
    AppMain.destroy()
    global edit_data_App
    edit_data_App = tkinter.Tk()
    edit_data_App.title("Modificando datos")
    screen_width = edit_data_App.winfo_screenwidth()
    screen_height = edit_data_App.winfo_screenheight()
    edit_data_App.geometry(f"{screen_width}x{screen_height}+200+0")
    edit_data_App.configure(background="#6C737E")  
    buttonBack = tkinter.Button(master=edit_data_App, text="Regresa", command=backMain5)
    buttonBack.place(relx=0.05, rely=0.05, anchor=tkinter.CENTER)

     # Configurar estilo personalizado
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#000000", foreground="#ffffff", fieldbackground="#1f497d")
    style.configure("Custom.Treeview.Heading", background="#000000", foreground="#ffffff", font=("Arial", 10, "bold"))

    # Cambiar el estilo predeterminado de ttk
    style.theme_use("default")  # Puedes probar diferentes estilos (clam, alt, default, etc.)

    table = ttk.Treeview(edit_data_App, columns=("Animales", "Sintomas", "Enfermedades", "Medicinas", "Doble click en la tabla"), style="Custom.Treeview")
    

    # Configurar encabezados de columna
    table.bind("<Double-Button-1>", doubleClickTable)
    table.heading("Animales", text="Animales", anchor="center")
    table.heading("Sintomas", text="Sintomas", anchor="center")
    table.heading("Enfermedades", text="Enfermedades", anchor="center")
    table.heading("Medicinas", text="Medicinas", anchor="center")
    table.heading("Doble click en la tabla", text="Doble click en la tabla", anchor="center")
    

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

def backMain2():
    mycursor.close()
    mydbd.close()
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
def updateTable():
    edit_data_App.destroy()
    selectDataApp.destroy()
    Main()
    

    



def Main():
    #interfaz principal
    
    #cargamos las imagenes
    AddImage = customtkinter.CTkImage(dark_image=Image.open(os.path.join("add_user_dark.png")), size=(20, 20))
    AskImage = customtkinter.CTkImage(dark_image=Image.open(os.path.join("chat_dark.png")), size=(20, 20))
    EditImage = customtkinter.CTkImage(dark_image=Image.open(os.path.join("edit.png")), size=(20,20))
    smartSearchImage = customtkinter.CTkImage(dark_image=Image.open(os.path.join("ai2.png")), size=(20,20))

    global AppMain
    AppMain = customtkinter.CTk()
    AppMain.title("Menu de opciones")
    #agregamos esta parte para que la ventana aparezca centrada y grande sin ningun problema
    screen_width = AppMain.winfo_screenwidth()
    screen_height = AppMain.winfo_screenheight()
    AppMain.geometry(f"{screen_width}x{screen_height}+0+0")

    AddAnimal = customtkinter.CTkButton(master= AppMain, text="Añadir animal, sintomas, enfermedad y medicina",fg_color="purple",image=AddImage, command=open_addAnimal)
    AddAnimal.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)


    askAnimalsAndSicks = customtkinter.CTkButton(master= AppMain, text="Ver animales y enfermedad", fg_color="green", image=AskImage, command=openAskAnimalsAndSicks)
    askAnimalsAndSicks.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)

    askAllAnimals = customtkinter.CTkButton(master= AppMain, text="Ver todos los datos", fg_color="green", image=AskImage, command=openAskAllAnimals)
    askAllAnimals.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)

    modifyData = customtkinter.CTkButton(master= AppMain, text = "Modificar o eliminar datos", fg_color="royalblue", image=EditImage, command=editData)
    modifyData.place(relx=0.45, rely=0.2, anchor=tkinter.CENTER)

    smartSearch = customtkinter.CTkButton(master= AppMain, text = "Busqueda inteligente ", fg_color="orange", image=smartSearchImage, command= deleteDataF)
    smartSearch.place(relx=0.45, rely=0.3, anchor=tkinter.CENTER)
    
    #imagen de fondo 
    bg_image = customtkinter.CTkImage(Image.open( "logo1.png"),
                                               size=(500, 400))
    bg_image_label = customtkinter.CTkLabel(image=bg_image, master=AppMain, text="")
    bg_image_label.place(relx=0.6, rely=0.2)
    AppMain.mainloop()


def connect():

    #parte de conexion a sql
    global mydbd
    global mycursor
    mydbd= mysql.connector.connect(host="127.0.0.1", user="root", password="aPERRITOMAN12", database="mascotas")
    mycursor= mydbd.cursor(buffered=True) #asi no sale el error al parecer las consultas tienen que ser liberadas con close y usar este buffered
    print("Conexion exitosa :D")


Main()