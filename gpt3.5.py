import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def create_prompt_of_reply_mail_generator(mail_content, reply_content, signature):
    if not signature:
        signature = "〇〇"
    messages = [
        {"role": "system", "content": "あなたはメールの返信文を日本語で書くアシスタントです。"},
        {
            "role": "user",
            "content": f"お相手から来た以下のメールに返信してください: 「{mail_content}」 返信の内容は 「{reply_content}」としてください。文末は「{signature}」としてください。",
        },
    ]
    return messages


mail_content = input("お相手からのメール文を入力してください")
reply_content = input("返信したい内容を入力してください")
signature = input("署名を入力してください")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=create_prompt_of_reply_mail_generator(
        mail_content, reply_content, signature
    ),
)

reply_mail = response["choices"][0]["message"]["content"]
print(reply_mail)
