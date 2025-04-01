import os
from flask import Flask, request, jsonify, render_template
from model import generate_image  
import logging
app = Flask(__name__, static_folder="static", template_folder=os.path.abspath("templates"))
logging.basicConfig(level=logging.INFO)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    text_input = data.get('text', '')
    print(text_input)
    app.logger.info(f"Received request with text: {text_input}")  # Log request
  

    # Call AI model to generate an image
    image_url = generate_image(text_input)

    return jsonify({"image_url": image_url})

if __name__ == '__main__':
    por = int(os.environ.get("PORT", 00cf883ee915782ee7cda21c46e7dc25))  # Get PORT from environment
    print(f"Starting Flask on port {por}...")
    app.logger.info(f"check is ok ")  # Log request
  
    app.run(host='0.0.0.0', port=por)
