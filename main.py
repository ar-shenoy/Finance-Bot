import json
with open('finance.json', 'r') as file:
    json_data = json.load(file)
def find_answer(question):
    question = question.lower()
    for data in json_data["questions"]:
        for keyword in data["keywords"]:
            if keyword.lower() in question:
                return data["answer"]
    return "Sorry, I don't have an answer to that question."

while True:
    user_question = input("Ask me a question (type 'quit' to exit): ")
    if user_question.lower() == 'quit':
        print("Goodbye!")
        break
    else:
        answer = find_answer(user_question)
        print("Answer:", answer)
