import cv2
import pytesseract

img = cv2.imread('/Users/hamadullah/Downloads/text_img.png')
cv2.imshow("new", img)
cv2.waitKey(0)


# Adding custom options
custom_config = r'--oem 3 --psm 6'
pytesseract.image_to_string(img, config=custom_config)