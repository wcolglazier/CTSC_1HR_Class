# pip install openai
import openai

#sk-
#proj-sgSm5vZ2zKVBYDp4u80tgi3dtmjo0W_YcDVPC8VL-15MbRLo3ZHu9rXdu7gwP1De1QoLzvAYTDT3BlbkFJ-RQcTwIGeP2FghCjNlQlmcSzJBLzQ0Yq12OxtSE-rWlWOvaXhWeW6GlH3gF-zRvI8Xm1kq00EA
openai.api_key = "key"


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
