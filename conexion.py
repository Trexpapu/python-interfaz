from sqlite3 import connect
import os
import mysql.connector
mydbd= mysql.connector.connect(host="*****", user="root", password="****", database="****")
mycursor= mydbd.cursor()
print("Conexion exitosa :D")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



def AllDates():

    try:
        animal = input("Ingrese el animal: ")
        
        # Realizar la consulta para verificar si ya existe un animal con ese nombre
        query = "SELECT ID_animal FROM animales WHERE Animal = %s"
        mycursor.execute(query, (animal,))
        
        # Obtener el resultado de la consulta
        result = mycursor.fetchone()
        
        if result:
            print("Ya existe un animal con ese nombre. Por favor, ingrese otro nombre.")
            input("Presiona Enter para continuar...")
            clear_console()
        else:
            sintomas = input("Ingrese los sintomas que presenta: ")
            enfermedad = input("Ingrese la enfermedad que va a agregar: ")
            medicina = input("Ingrese la medicina que va a agregar: ")
            
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
            print("Datos ingresados correctamente")
            input("Presiona Enter para continuar...")
            clear_console()

    except mysql.connector.IntegrityError:
        print("Ya existe un animal con ese nombre. Por favor, ingrese otro nombre.")
        input("Presiona Enter para continuar...")
        clear_console()

def AddDatesToAnimal():
    nombre_animal=input("Ingrese el nombre del animal al cual va a agregar datos: ") 
    # Realizar la consulta para obtener el ID del animal por su nombre
    query = "SELECT ID_animal FROM animales WHERE Animal = %s"
    mycursor.execute(query, (nombre_animal,))
    result = mycursor.fetchone()
    if result:
        id_animal=result[0]
        sintomas = input("Ingrese los sintomas que presenta: ")
        enfermedad = input("Ingrese la enfermedad que va a agregar: ")
        medicina = input("Ingrese la medicina que va a agregar: ")
        mycursor.execute("INSERT INTO medicinas(Medicina) VALUES(%s)", (medicina,))
        id_medicina = mycursor.lastrowid
        mycursor.execute("INSERT INTO enfermedades(Enfermedad, ID_medicina) VALUES(%s, %s)", (enfermedad, id_medicina))
        id_enfermedad = mycursor.lastrowid
        mycursor.execute("INSERT INTO sintomas(Sintomas, ID_animal, ID_enfermedad) VALUES(%s, %s, %s)", (sintomas, id_animal, id_enfermedad))
        # Confirmar los cambios realizados en la base de datos
        mydbd.commit()
        print("Datos ingresados correctamente")
        input("Presiona Enter para continuar...")
        clear_console()

        

    else:
        print("No existe un animal con ese nombre, agrega uno en la opcion 1...")
        input("Presiona Enter para continuar...")
        clear_console()

def ShowAllDates():
    print("//////////Tabla animales/////////////")
    mycursor.execute("SELECT * FROM animales")
    column_names = [desc[0] for desc in mycursor.description]
    print(column_names)
    for i in mycursor:
        print(i)
    print("//////////////Tabla sintomas////////////")
    mycursor.execute("SELECT * FROM sintomas")
    column_names = [desc[0] for desc in mycursor.description]
    print(column_names)
    for i in mycursor:
        print(i)
    print("/////////////Tabla enfermedades//////////////////7")
    mycursor.execute("SELECT * FROM enfermedades")
    column_names = [desc[0] for desc in mycursor.description]
    print(column_names)
    for i in mycursor:
        print(i)
    print("///////////////Tabla medicinas//////////////////")
    mycursor.execute("SELECT * FROM medicinas")
    column_names = [desc[0] for desc in mycursor.description]
    print(column_names)
    for i in mycursor:
        print(i)
    input("Presiona Enter para continuar...")
    clear_console()

def ShowAnimal():
    nombre_animal = input("Ingrese el nombre del animal que busca: ")

    # Realizar la consulta para obtener el ID del animal por su nombre
    query = "SELECT ID_animal FROM animales WHERE Animal = %s"
    mycursor.execute(query, (nombre_animal,))
    result = mycursor.fetchone()

    if result:
        id_animal = result[0]

        query = """
            SELECT a.Animal, s.Sintomas, e.Enfermedad, m.Medicina
            FROM animales AS a
            JOIN sintomas AS s ON a.ID_animal = s.ID_animal
            JOIN enfermedades AS e ON s.ID_enfermedad = e.ID_enfermedad
            JOIN medicinas AS m ON e.ID_medicina = m.ID_medicina
            WHERE a.ID_animal = %s
        """
        mycursor.execute(query, (id_animal,))
        results = mycursor.fetchall()

        if results:
            for row in results:
                animal = row[0]
                sintomas = row[1]
                enfermedad = row[2]
                medicina = row[3]
                print("Animal:", animal)
                print("Síntomas:", sintomas)
                print("Enfermedad:", enfermedad)
                print("Medicina:", medicina)
                print("---")
        else:
            print("No se encontraron resultados para el animal:", nombre_animal)
    else:
        print("No existe un animal con ese nombre, agrega uno en la opción 1...")
    
    input("Presiona Enter para continuar...")
    clear_console()


def ShowAnimalWithSick():
    nombre_animal = input("Ingrese el nombre del animal que busca: ")

    # Realizar la consulta para obtener el ID del animal por su nombre
    query = "SELECT ID_animal FROM animales WHERE Animal = %s"
    mycursor.execute(query, (nombre_animal,))
    result1 = mycursor.fetchone()


    nombre_enfermedad = input("Ingrese el nombre de la enfermedad del animal que busca: ")

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
            for row in results:
                animal = row[0]
                sintomas = row[1]
                enfermedad = row[2]
                medicina = row[3]
                print("Animal:", animal)
                print("Síntomas:", sintomas)
                print("Enfermedad:", enfermedad)
                print("Medicina:", medicina)
                print("---")
        else:
            print("No se encontraron resultados para el animal o enfermedad:", nombre_animal, nombre_enfermedad)
    else:
        print("No existe un animal o enfermedad con ese nombre...", nombre_animal, nombre_enfermedad)
    
    input("Presiona Enter para continuar...")
    clear_console()





finalizar=True
print("BIENVENICO A LA DB DE MASCOTAS")
while finalizar == True:
    
    print("1. Agregar los datos animal, sintomas, enfermedad y medicina")
    print("2. Agregar sintomas, enfermedad y medicina a un animal ya agregado")
    print("3. Mostrar informacion de todos los animales")
    print("4. Mostrar informacion de un animal ")
    print("5. Mostrar informacion de un animal y una enfermedad")
    print("6. Borrar datos de un animal")
    print("7. Borrar datos de una enfermedad, sintomas y medicina")
    print("8. Para modificar datos de un animal, enfermedad, sintomas o medicina")
    print("9. Salir")
    

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        AllDates()
        
    elif opcion == "2":
        AddDatesToAnimal()
        
        
    elif opcion == "3":
        ShowAllDates()

    elif opcion == "4":

        ShowAnimal()
    elif opcion == "5":
        
        ShowAnimalWithSick()
    elif opcion == "6":
        print("")
    elif opcion == "7":
        print("")
    elif opcion == "9":
        print("Has salido") 
        finalizar=False
        mydbd.close()  
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
