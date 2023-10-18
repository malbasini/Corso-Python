import openai
from decouple import config
openai.api_key=config("OPENAI_API_KEY")
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"user","content":"Chi ha sviluppato Python?"}
    ])
print(completion.choices[0].message.content)
