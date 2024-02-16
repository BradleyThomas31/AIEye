from openai import OpenAI

client = OpenAI(api_key='INSERT HERE')

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "How many carbohydrates in this?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://www.fda.gov/files/nfl-howtounderstand-pretzels.png",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
