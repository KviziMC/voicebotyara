from groq import Groq
client = Groq(api_key='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')
promt = input('Запитайте щось мене: \n')
def generate(promt):
    chat_completion = client.chat.copletions.create(
        messages=[
            {
                'role': 'user',
                'content': promt,
            }
        ],
        model='llama3-8b-8192',
    )
    return chat_completion.choices[0].message