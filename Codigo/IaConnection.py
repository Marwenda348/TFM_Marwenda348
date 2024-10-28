import Componentes
from openai import OpenAI



client = OpenAI(api_key=Componentes.ApiOpen)
def Preguntar(self):

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=10,
        messages=[
            {"role": "user", "content": "No puedes contestar a otra cosa que no sea : Es esto una IP o un Dominio valido, necesito que la respuesta empiece por Si o No" + self}
        ]
    )

    Respuesta=completion.choices[0].message.content
    print(Respuesta)

