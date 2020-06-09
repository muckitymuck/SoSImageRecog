from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# https://github.com/UB-Mannheim/tesseract/wiki

def receiptRead(receipt):
    im = pytesseract.image_to_string(Image.open(receipt))

    # text = pytesseract.image_to_string(im)
    return im

print(receiptRead('receipt2.jpg'))