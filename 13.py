import json
from difflib import get_close_matches

print("Hey!")

def load_knowledge_base(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            data = file.read().strip()
            if not data:
                data = {"questions": []}
                save_knowledge_base(file_path, data)
            else:
                data = json.loads(data)
    except FileNotFoundError:
        data = {"questions": []}
        save_knowledge_base(file_path, data)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

def chatbot():
    knowledge_base = load_knowledge_base('knowledge_base.json')

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            break

        best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot: {answer}")
        else:
            print("Bot: I don't know the answer to that question. Can you please provide the answer?")
            new_answer = input("You: ")
            knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
            save_knowledge_base('knowledge_base.json', knowledge_base)
            print("Bot: Thank you! I've learned a new answer.")

if __name__ == "__main__":
    chatbot()