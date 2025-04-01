# import random

# def generate_image(text):
#     # Placeholder function: Replace with actual GAN model
#     sample_images = [
#         "https://via.placeholder.com/400?text=Image+1",
#         "https://via.placeholder.com/400?text=Image+2",
#         "https://via.placeholder.com/400?text=Image+3"
#     ]
#     return random.choice(sample_images)

# import requests

# # Your Hugging Face API Key
# API_KEY = "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"



# MODEL_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

# def generate_image(prompt):
#     headers = {"Authorization": f"Bearer {API_KEY}"}
#     payload = {"inputs": prompt}

#     response = requests.post(MODEL_URL, headers=headers, json=payload)

#     if response.status_code == 200:
#         with open("realistic_image.png", "wb") as f:
#             f.write(response.content)
#         return "realistic_image.png"
#     else:
#         return f"Error: {response.status_code}, {response.text}"

# if __name__ == "__main__":
#     prompt_text = input("Enter a prompt: ")
#     result = generate_image(prompt_text)
#     print(f"Image saved as {result}" if "png" in result else result)

import requests
import os

# Hugging Face API credentials
API_KEY = "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"
MODEL_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

# Ensure 'static/generated' folder exists to store images
IMAGE_DIR = "static/generated"
os.makedirs(IMAGE_DIR, exist_ok=True)

def generate_image(prompt):
    """Generates an image from text and saves it in static folder"""
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"inputs": prompt}

    response = requests.post(MODEL_URL, headers=headers, json=payload)

    if response.status_code == 200:
        image_filename = f"generated_image.png"  # You can modify this to unique names
        img_path = os.path.join(IMAGE_DIR, image_filename)
        with open(img_path, "wb") as f:
            f.write(response.content)
        
        # Return only the image path (Flask will serve it)
        return get_image_url(image_filename)
    else:
        return None
    
def get_image_url(image_filename):
    """Returns the complete URL of the generated image"""
    return f"/static/generated/{image_filename}"  
