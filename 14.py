# pip install openai
import openai

openai.api_key = "key"
# sk-
# proj-4y6uR7PpcLhF2iXLoFrd-1AIB-YAFOVQHP3Kqec8w2yAnaLtQWA8itGAxoS1GOe6YR7rf15IvvT3BlbkFJXjObu0va910pBdDzvMh4HlZicuVwnFKcrE47fyKAKqQ4CM0mkDxiecZTrSCfasUDhQWXSUHvgA

def bot(user_input, messages):
    messages.append({"role": "user", "content": user_input})

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": message})
    return message, messages


if __name__ == '__main__':
    messages = [
        {"role": "system", "content": """


        """}
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Session ended.")
            break

        response, messages = bot(user_input, messages)
        print("Assistant:", response)
