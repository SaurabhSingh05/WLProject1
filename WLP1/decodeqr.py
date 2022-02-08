

import cv2

detect = cv2.QRCodeDetector()

reval, point, s_qr = detect.detectAndDecode(cv2.imread('7Febsecondfile.jpg'))

print(reval)