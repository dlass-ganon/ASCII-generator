from PIL import Image

symbols = [" ", ".", "·", "+", "°", "o", "*", "¤", "@", "#"]

def ASCII_gen(image_path, new_width=100):
    
    img = Image.open(image_path).convert("L")
    
    original_width, original_height = img.size
    aspect_ratio = original_height / original_width
    
    pixels = list(img.getdata())
    
    ascii_chars = [symbols[pixel // 32] for pixel in pixels]
    ascii_str = "".join(ascii_chars)
    
    pixel_count = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:(i + original_width)] for i in range(0, pixel_count, original_width)])
    
    return ascii_img

result = ASCII_gen("your.png")
print(result)