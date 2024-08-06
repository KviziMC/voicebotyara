from groq import Groq
client = Groq(api_key='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')

def generate(promt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': promt,
            }
        ],
        model='llama3-8b-8192',
    )
    return chat_completion.choices[0].message