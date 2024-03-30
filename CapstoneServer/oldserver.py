from llm import get_chat_completion
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        data = request.json 
        user_input = data.get('inputText', 'No Input Received')
        print(user_input)  
        model = "gpt-4-vision-preview"
        api_key = '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'
        image_url = "https://img.restaurantguru.com/r3b6-no-246-menu-2022-10-2.jpg"
        processed_input = get_chat_completion(api_key, model, user_input, image_url)

        # Ensure processed_input is a string
        processed_input_str = str(processed_input)

        # Return combined JSON response
        return jsonify({'response': processed_input_str})

#        return jsonify({'response': user_input, 'processed': processed_input_str})

    else:
        return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)

