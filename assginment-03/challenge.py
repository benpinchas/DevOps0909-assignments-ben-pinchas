from PIL import Image, ImageDraw

# Image dimensions
IMG_WIDTH = 800
IMG_HEIGHT = 200

# Instansiate objects
img = Image.new(
   mode='RGB', 
   size=(IMG_WIDTH, IMG_HEIGHT), 
   color="papayawhip"
)
d = ImageDraw.Draw(img)

# Perform some work
d.text(
   xy=(IMG_WIDTH/2-30, IMG_HEIGHT/2-5), 
   text="Hello DevOps0909", 
   fill="red",
)

# Save image
img.save('my-image.png')