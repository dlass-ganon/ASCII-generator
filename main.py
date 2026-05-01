from PIL import Image

symbols = [" ", ".", "·", "+", "°", "o", "*", "¤", "@", "#"]

def ASCII_gen(image_path, new_width=100):
    
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

result = ASCII_gen("your.png")

def save_as_html(ascii_img, filename="output.html"):
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                background-color: #000; /* Black background */
                color: #fff;            /* White text */
                font-family: 'Courier New', monospace;
                line-height: 8px;       /* Tighten line height */
                letter-spacing: 0px;
                white-space: pre;       /* Keeps spaces/newlines */
            }}
        </style>
    </head>
    <body>
{ascii_img}
    </body>
    </html>
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved to {filename}")