#Importamos libreria de REgex
import re

#Definimos la función a utilizar
def whitelist(self):
#Reccoremos el String introducido
    for i in self:
        #Comprobamos letra a letra que esta en la Whitelist
        Whitelist = re.search(r"[a-zA-Z0-9./]",i)
        #Si no lo esta se devuelve None
        if not Whitelist:
            return None
    #Si llegamos aqui quiere decir que todas las letras estan en el whitelist
    #por lo que podemos devolver el texto como vino
    if Whitelist:
        #Comprobamos si es un dominio que empieza por letras o numeros de 1 a 63 caracteres, tiene un punto y solo letras de 2 a 6 caracteres
        dominio_regex = re.compile(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}$")
        #Utilizamos regex también para valorar que es una IP valida
        ip_regex = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        if (dominio_regex.match(self)) or (ip_regex.match(self)) :
            print("Dominio o IP valida con formato correcto")
            return self 
    
def DominioValido(self):
    Domain=whitelist(self)
    if Domain :
        return 1
    else:
        return 0  