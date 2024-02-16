import random
from PIL import Image

def randomize(image_path, output_path):
    # Open an image file
    img = Image.open(image_path)

    # Get the pixel data
    pixels = img.load()

    # Iterate through each pixel and invert its color
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            random_amount = 300
            pixels[x, y] = (r-random_amount + random.randint(0,2*random_amount), g-random_amount + random.randint(0,2*random_amount), b-random_amount + random.randint(0,2*random_amount))

    # Save the modified image
    img.save(output_path)

def invert_image(image_path, output_path):
    # Open an image file
    img = Image.open(image_path)

    # Get the pixel data
    pixels = img.load()

    # Iterate through each pixel and invert its color
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (255 - r, 255 - g, 255 - b)

    # Save the modified image
    img.save(output_path)

# Example usage
input_path = "pixel_manipulation/trump.jpg"
output_path = "pixel_manipulation/2.jpg"
randomize(input_path, output_path)
#invert_image(input_path, output_path)