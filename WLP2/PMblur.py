from PIL import Image, ImageFilter

img1 = Image.open("cat1.jpg")
# image Blur

img1.filter(ImageFilter.GaussianBlur(radius=4)).save('cat1blur.jpg')