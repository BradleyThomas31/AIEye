from flask import Flask, request, jsonify
from PIL import Image
import base64
import requests
import io
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image_file = request.files['image']
    temp_image_path = os.path.join('temp', image_file.filename)
    image_file.save(temp_image_path)

    input_text = request.form.get('inputText', '') 
    print(f'Received input text ugh: {input_text}') 

    with open(temp_image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode('utf-8')

    api_key = "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"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    query = f"Answer in 5 words: How many verbs are in the following text?"
    payload = {
      "model": "gpt-4-turbo",
      "messages": [
      { "role": "user",
      "content": [
        {
          "type": "text",
          "text":  input_text
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    os.remove(temp_image_path)
    print(response)
   
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

