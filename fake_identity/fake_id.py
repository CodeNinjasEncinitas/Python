from faker import Faker
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import requests
import time

# generate name
fake = Faker(['en_US']) # nationality and language
prefix = fake.prefix() # Prefix (e.g., Mr., Mrs.)
first_name = fake.first_name()
last_name = fake.last_name()

# create blank image to start
image = Image.new("RGB", (800, 600))

# generate random person image
fileName = "random_person_image.jpg"
f = open(fileName,'wb')
f.write(requests.get('https://thispersondoesnotexist.com', headers={'User-Agent': 'My User Agent 1.0'}).content)
f.close()

# paste blank_id_template onto image
blank_id_template = Image.open('blank_id_template.jpg')
image.paste(blank_id_template, (0, 0))

# resize, crop, then paste random_person_image onto image in main photo spot
offset = (43, 80)
random_person_image = Image.open('random_person_image.jpg')
new_width = 255
new_height = 290
new_size = (new_width, new_height)
crop_left = 20
crop_right = 20
resized_image = random_person_image.resize(new_size)
cropped_image = resized_image.crop((crop_left, 0, new_size[0] - crop_right, new_size[1]))
image.paste(cropped_image, offset)

# resize, crop, then paste random_person_image in black & white onto image in tiny photo spot
offset = (470, 265)
random_person_image = Image.open('random_person_image.jpg')
new_width = 120
new_height = 120
new_size = (new_width, new_height)
crop_left = 20
crop_right = 20
resized_image = random_person_image.resize(new_size)
cropped_image = resized_image.crop((crop_left, 0, new_size[0] - crop_right, new_size[1]))
bw_image = cropped_image.convert("L")
image.paste(bw_image, offset)

# add fake signature
draw = ImageDraw.Draw(image)
text = first_name + " " + last_name
font = ImageFont.truetype("fonts/Cursive.ttf", 31)  # You can change the font and size as needed
text_position = (40, 380)  # Adjust as needed
draw.text(text_position, text, fill="black", font=font)


# add a license number
draw = ImageDraw.Draw(image)
text = "H5189946"
font = ImageFont.truetype("fonts/FreeSansBold.ttf", 28.5)  # You can change the font and size as needed
text_position = (300, 80)  # Adjust as needed
draw.text(text_position, text, fill="red", font=font)

# add expiration date
draw = ImageDraw.Draw(image)
text = "1/23/2045"
font = ImageFont.truetype("fonts/FreeSansBold.ttf", 28.5)  # You can change the font and size as needed
text_position = (320, 120)  # Adjust as needed
draw.text(text_position, text, fill="red", font=font)

# add last name
draw = ImageDraw.Draw(image)
print(last_name.upper())
text = last_name.upper()
font = ImageFont.truetype("fonts/FreeSansBold.ttf", 28.5)  # You can change the font and size as needed
text_position = (300, 160)  # Adjust as needed
draw.text(text_position, text, fill="black", font=font)

# add first name
draw = ImageDraw.Draw(image)
text = first_name.upper()
font = ImageFont.truetype("fonts/FreeSansBold.ttf", 28.5)  # You can change the font and size as needed
text_position = (300, 200)  # Adjust as needed
draw.text(text_position, text, fill="black", font=font)


# show the image!
image.show()
 
# Save the edited image
#id_img.save("car2.png")

