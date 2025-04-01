import os
from flask import Flask, request, jsonify, render_template
from model import generate_image  

app = Flask(__name__, static_folder="static", template_folder=os.path.abspath("templates"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    text_input = data.get('text', '')
    print(text_input)

    # Call AI model to generate an image
    image_url = generate_image(text_input)

    return jsonify({"image_url": image_url})

if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 4000))  # Get PORT from environment
    print(f"Starting Flask on port {port}...")
    app.run(host='0.0.0.0', port=4000)
