from PIL import Image, ImageDraw, ImageFont

import math

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]            # Define the characters to use for ASCII art

charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

scaleFactor = 0.005                                                                                 # Set the scaling factor for the image

oneCharWidth = 10
oneCharHeight = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

text_file = open("Output.txt", "w")                                                                 # Open a text file to save the ASCII characters

im = Image.open("naruto.jpg").convert('RGB')

fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()

outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))       # Create a new image to store the ASCII art output
d = ImageDraw.Draw(outputImage)

for i in range(height):                                                                                 # Process each pixel of the resized image
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))                                                                     # Write the corresponding character to the text file
        d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))             # Draw the character on the output image

    text_file.write('\n')

outputImage.save('output.png')                                                                          # Save the generated ASCII art image and close the text file
