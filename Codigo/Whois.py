import subprocess
import json

#Definimos como vamos a convertir los datos de texto plano en objeto para Json
def parsear(resultado):
    Datos= {}
    for linea in resultado.splitlines():
        if ":" in linea:
            # Dividir la línea en clave y valor
            clave, valor = linea.split(":", 1)
            Datos[clave.strip()] = valor.strip()
    return Datos

def whois(Dominio):
    try:
        resultado = subprocess.run(["whois", Dominio], check=True, capture_output=True, text=True) 
        revisar= parsear(resultado.stdout)
        with open("whois.json", "w") as file:
            json.dump(revisar, file, indent=4)
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el comando:", e)