import sys
import openai
from decouple import config
openai.api_key=config("OPENAI_API_KEY")
#Quarto esempio una conversazione tra l'utente e l'assistente virtuale con tono da teenager
def chat_with_openai():
    chat_history=[]
    chat_history.append({"role":"system", "content":"Usa un tono da teenager."})
    while True:
        user_input=input("User:" )
        chat_history.append({"role":"user","content":user_input})
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history
        )
        assistant_response=response.choices[0].message.get("content")
        print("Assistant:", assistant_response)
        chat_history.append({"role": "assistant", "content": assistant_response})
        if user_input.lower()=="fine":
            sys.exit()
chat_with_openai()

