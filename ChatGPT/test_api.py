import openai
from decouple import config
openai.api_key=config("OPENAI_API_KEY")
#Primo esempio con la classe Completion
def test_api():
    risposta=openai.Completion.create(
        engine="text-davinci-002",
        prompt="Quanti abitanti ha Roma?",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.9
    )
    print(risposta.choices[0].text.strip())
test_api()