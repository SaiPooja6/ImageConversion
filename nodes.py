"""
This is a boilerplate pipeline 'newpipeline'
generated using Kedro 0.19.8
"""
from PIL import Image, ImageDraw

#Creating a node by defining a function for converting the colored image to grayscaled image.

def grayscale_image(image: Image.Image)->Image.Image:
    image = image.convert("L")
    return image

#Creating a node by defining a function for a grayscaled image turns to 100*100 size.

def size_conversion(image: Image.Image)->Image.Image:
    image = image.resize((200, 200))
    return image

#Creating a node by defining a function for adding a text to grayscale resized image.

def adding_text(image: Image.Image)->Image.Image:
    draw = ImageDraw.Draw(image)
    text = "Hello. How can I help you?"
    position = (10,170)
    font_size = 16
    draw.text(position, text, fill = "red")
    return image




    

