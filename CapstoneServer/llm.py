from openai import OpenAI

def get_chat_completion(api_key, model, user_text, image_url):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_text},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content

api_key = "X"
model = "gpt-4-vision-preview"
user_text = "Is there a steak on the menu?? (Answer in 20 words or less)"
image_url = "https://img.restaurantguru.com/r3b6-no-246-menu-2022-10-2.jpg"
response_content = get_chat_completion(api_key, model, user_text, image_url)
print(response_content)
