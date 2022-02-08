# Generating QR Code Method1
'''
import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=TFW21ylLvU0")

img.save('youtubeMJO.png')
'''

# Generating QR Code Method2

import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("New students have been added to QRCode Group: Student Name: Aniket & Mohit Painwal")
qr.make(fit=True)
img2 = qr.make_image(fill_color='red', backcolor='white')

img2.save("7Febsecondfile.jpg")
