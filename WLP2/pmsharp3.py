# Sharpness

from PIL import Image, ImageEnhance
import os

img1 = Image.open("cat1.jpg")
enhanceimg = ImageEnhance.Sharpness(img1)
enhanceimg.enhance(4).save('sharp\cat1.jpg')

# Sharpness
# 0 : Blurry
# 1:  Original Image
# 2:  Image with incresed sharpness
# 3: now sharpness is increasing

# Color
# 0. Black & White
# 1. Original Colors
# 2. Colors will increase 

# Brightness
# 0. Black
# 1. Original brightness
# 2. Brightness will increase 

