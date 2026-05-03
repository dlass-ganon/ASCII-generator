from PIL import Image

import os

from flask import Flask, render_template
app = Flask(__name__)

Image_folder =  os.path.join("static", "assets") #idetifies the folders
Image_path = os.path.join(Image_folder, "demon.jpeg") 

symbols = [" ", ".", "·", "+", "°", "o", "*", "¤", "@", "#"]

def ASCII_gen(image_path, new_width=115):
    
    img = Image.open(image_path).convert("L")
    
    original_width, original_height = img.size
    aspect_ratio = original_height / original_width
    new_height = int(aspect_ratio * new_width * 0.5)
    img = img.resize((new_width, new_height))
    
    pixels = list(img.getdata())
    
    ascii_chars = [symbols[pixel // 32] for pixel in pixels]
    ascii_str = "".join(ascii_chars)
    
    pixel_count = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:(i + new_width)] for i in range(0, pixel_count, new_width)])
    
    return ascii_img

result = ASCII_gen(Image_path)

@app.route('/')
def home():
    my_text = result
    return render_template('index.html', display_text=my_text)

if __name__ == "__main__":
    app.run(port=5000, debug=True)