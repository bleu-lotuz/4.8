# importing PIL.Image library and os library
from PIL import Image
import os
 
# Deletes old created images if they exist
if os.path.exists("newImage.jpg"):
  os.remove("newImage.jpg")
 
# Prints two blank lines to start our program output
print("\n\n")
 
# Opens image - Local File in repl.it
img = Image.open('image.jpg')
 
# Rescale image size down, if needed
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
  scale = mwidth
else:
  scale = mheight
if scale != 0:
  img = img.resize( (width // scale, height // scale) )
 
########################
#        Filter        #
########################
def newFilter():
  color = input("What color do you want your image to be: red, green or blue? ")
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
 
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = r
    newg = g
    newb = b
 
    if color == "red":
      newr = r * 10
    elif color == "green":
      newg = g * 10
    elif color == "blue":
      newb = b * 10
    else:
      print("You did not choose a correct option.")
 
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
 
  # Creates a new image, the same size as the original
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the pixel values to newImage
  newImage.putdata(new_pixels)
  # Saves the new image file
  newImage.save("newImage.jpg")
 
# Creates an ImageCore Object from original image
pixels = img.getdata()
# Creates empty array to hold new pixel values
new_pixels = []
# For every pixel from our original image, it saves
# a copy of that pixel to our new_pixels array
for p in pixels:
  new_pixels.append(p)
 
p = new_pixels[location]
    # Splits color into red, green and blue components
r = p[0]
g = p[1]
b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
newr = r
newg = g
newb = b

value = int(input("Enter your favorite color between red, green, or blue: "))

if value == "red":
      newr = r * 10
      elif value == "green":
      newg = g * 10
      elif value == "blue":
      newb = b * 10
      else:
      print("You did not choose a correct option.")

# Calls the newFilter function to create the image
newFilter()