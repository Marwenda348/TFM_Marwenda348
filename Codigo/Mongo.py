from pymongo import MongoClient
from Componentes import Usermdb, Passmdb


#Conectamos a la Base de datos con los valores importados de Componentes
uri = "mongodb://" + Usermdb + ":" + Passmdb + "@localhost:27017/test?authSource=admin"
cliente = MongoClient(uri)
db = cliente['Escaneos']
coleccion = ""
        

def Añadir(Nombre,Texto):
    #Forzamos que sea un string
    coleccion = db[str(Nombre)]
    # Datos JSON, aqui ira el Texto que enviaremos desde main.
    datos = [Texto]
    # Insertar documentos
    try:
        resultado = coleccion.insert_many(datos)
        print(f"Documentos insertados con IDs: {resultado.inserted_ids}")
    except Exception as e:
        print(f"Error al insertar los documentos: {e}")

def Listartodo(Nombre):
    coleccion = db[str(Nombre)]
    Valor = coleccion.find()
    # Imprimir cada documento
    for Unidad in Valor:
        print(Unidad)



