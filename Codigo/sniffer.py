import subprocess
import json


def whois(Dominio):
    try:
        resultado = subprocess.run(["whois", Dominio], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el comando:", e)
    with open('Total.json', 'w') as file:
        json.dump(resultado, file, indent=4)


whois(input)