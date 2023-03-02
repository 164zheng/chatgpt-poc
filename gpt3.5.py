import os
import openai
import mypy

openai.api_key = os.getenv("OPENAI_API_KEY")


def create_prompt_of_mail_generator(mail_content):
    pass


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "あなたは会社の秘書です"},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {
            "role": "assistant",
            "content": "The Los Angeles Dodgers won the World Series in 2020.",
        },
        {"role": "user", "content": "Where was it played?"},
    ],
)

print(response)
