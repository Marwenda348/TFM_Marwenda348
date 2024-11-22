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
            max_tokens=10, #Numero de caracteres en la respuesta
            messages=[#Parametros
                {"role": "user", "content": "No puedes contestar a otra cosa que no sea : Es esto una IP o un Dominio valido, necesito que la respuesta sea Si o No" + self}
            ]
        )
        #Seleccionamos solo la respuesta que nos interesa.
        Respuesta=completion.choices[0].message.content
        return Respuesta
#Manejamos los errores de Conexion        
except OpenAIError as e:
     print('Error: {}'.format(e))
