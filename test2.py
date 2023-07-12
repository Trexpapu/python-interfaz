import tkinter as tk

def obtener_valores():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    mensaje = f"¡Hola, {nombre} {apellido}!"
    label_mensaje.config(text=mensaje)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("300x200")

# Crear etiquetas y campos de entrada
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_apellido = tk.Label(ventana, text="Apellido:")
label_apellido.pack()
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

# Botón para obtener los valores
btn_obtener_valores = tk.Button(ventana, text="Obtener Valores", command=obtener_valores)
btn_obtener_valores.pack()

# Etiqueta para mostrar el mensaje
label_mensaje = tk.Label(ventana, text="")
label_mensaje.pack()

# Iniciar el bucle de eventos
ventana.mainloop()
