from flask import Flask, request, jsonify
from PIL import Image
import base64
import requests
import os
import pytesseract
import traceback

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def imageToText():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    print("bbb")
    # Save the image temporarily
    image_file = request.files['image']
    temp_image_path = os.path.join('temp', image_file.filename)
    image_file.save(temp_image_path)
    try:
        print("ccc")
        # Use Pytesseract to convert the image to text
        text = pytesseract.image_to_string(Image.open(temp_image_path))
        print("ddd")
        print(text)
        # Clean up: remove the temporary saved image
        # os.remove(temp_image_path)

        return jsonify({'text': text}), 200
    except Exception as e:
        # Print the full stack trace
        traceback.print_exc()
        # Clean up and handle errors
        os.remove(temp_image_path)
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    # Save the image temporarily
    image_file = request.files['image']
    temp_image_path = os.path.join('temp', image_file.filename)
    image_file.save(temp_image_path)

    # Encode the image in base64
    with open(temp_image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode('utf-8')

    # Prepare headers and payload for OpenAI API
    api_key = "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"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What’s in this image?"
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

    # Make the request to OpenAI API
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # Remove the temporary image to clean up
    os.remove(temp_image_path)

    # Return the response from OpenAI API to the client
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

