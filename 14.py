# pip install openai
import openai

openai.api_key = "key"

#proj-hRkPxOQ82ncDr64Ucdbgm52FVYhBM7eqev2yieRjIQ29RbwaI64bG2SMO0PHtd5-TbDoERMQIaT3BlbkFJBMv8NjPJcSqp66MRnfhMdDobmU2PxKKo9Vt5P5uF87wjfN_-tFjZWBlggUos22nbKxzIYnjDwA



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
