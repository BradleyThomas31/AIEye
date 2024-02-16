from openai import OpenAI

client = OpenAI(api_key='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')

def ask_question(question):
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question},
    ])
    answer = response.choices[0].message.content
    return answer

question = "What is the capital of France?"
answer = ask_question(question)
print(f"Question: {question}\nAnswer: {answer}")

