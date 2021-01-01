import cv2
import pytesseract
from preprocessing import get_grayscale,thresholding,opening,dilate,sharpen,erode

def show(img):
    cv2.imshow("window",img)
    cv2.waitKey(0)


def preprocess(img):
    img = thresholding(get_grayscale(img))
    img = sharpen(img)
    img = cv2.fastNlMeansDenoising(img,h=55)
    return img

def predict(img):
    custom_config = r'--oem 3 --psm 13'
    print(pytesseract.image_to_string(img, config=custom_config))

def final_predict(img):
    img = preprocess(img)
    show(img)
    predict(img)

if __name__ == "__main__":
    img = cv2.imread('test-imgs/email.jpeg')
    final_predict(img)