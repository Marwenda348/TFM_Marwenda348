import tkinter as tk

def get_ip():
    global ip_address  # Declarar como global para poder usarla fuera de la función
    ip_address = str(ip_entry.get())  # Obtener el valor ingresado
    root.destroy()  # Cerrar la ventana después de guardar la IP
# Variable para almacenar la IP
ip_address = None

# Configuración de la ventana
root = tk.Tk()
root.title("Ingreso de IP")
root.geometry("300x150")

# Etiqueta
label = tk.Label(root, text="Por favor, ingrese una dirección IP:")
label.pack(pady=10)

# Campo de entrada
ip_entry = tk.Entry(root, width=20)
ip_entry.pack(pady=5)

# Botón de enviar
submit_button = tk.Button(root, text="Enviar", command=get_ip)
submit_button.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
