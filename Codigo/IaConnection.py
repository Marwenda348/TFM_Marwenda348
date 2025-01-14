from Componentes import ApiOpen 
from openai import OpenAI , OpenAIError

#Establecemos conexión con el servidor de Openai
try:
    client = OpenAI(api_key=ApiOpen)
    #Creamos una función para preguntar si el Dominio es valido
    def Preguntar(self):
        #Conectamos
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo", #indicamos que modelo de Chat queremos
            max_tokens=2, #Numero de caracteres en la respuesta
            messages=[#Parametros
                {"role": "user", "content": "No puedes contestar a otra cosa que no sea : ¿Es esto una IP o un Dominio valido" + self +"?, necesito que la respuesta sea solamente Si o No"}
            ]
        )
        #Seleccionamos solo la respuesta que nos interesa.
        Respuesta=completion.choices[0].message.content
        return Respuesta
    
    def Informe(Informe):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo", #indicamos que modelo de Chat queremos
            max_tokens=3000, #Numero de caracteres en la respuesta
            messages=[#Parametros
                {"role": "user", "content": "Para ayudar al tecnico de seguridad que se encarga de esta auditoria "+ 
                 "queremos que con la información adjuntada aqui"+str(Informe)+" elabores un informe"+ 
                 "de vulnerabilidades. Para ello primero pon la información relevante de la empresa, después todos"+
                 "los servicios corriendo con el software especifico y listado de cve más peligrosos" }
            ]

        )
        Respuesta=completion.choices[0].message.content
        return Respuesta
    def Cve(CVES):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo", #indicamos que modelo de Chat queremos
            max_tokens=300, #Numero de caracteres en la respuesta
            messages=[#Parametros
                {"role": "user", "content": "Para ayudar al tecnico de seguridad que se encarga de esta auditoria "+ 
                 "necesito que me analices la siguiente CVE, Necesito que sigas el siguiente patron, Que CVE tiene la vulnerabilidad, salto de linea,  Explicacion: "+
                 "aqui la explicacion del CVE, salto de linea,Solucion: aqui como lo solucionarias "+CVES }
            ]

        )
        Respuesta=completion.choices[0].message.content
        return Respuesta
#Manejamos los errores de Conexion        
except OpenAIError as e:
     print('Error: {}'.format(e))



