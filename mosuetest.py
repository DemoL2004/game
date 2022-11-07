import mouse as m
import pyautogui as pyg
import time as t
from pynput.mouse import Button
from PIL import ImageGrab
from PIL import Image
from pytesseract import pytesseract
#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract
pyg.keyDown("alt")
pyg.press("tab")
pyg.keyUp("alt")
t.sleep(3)
ss_region = (930,495,980,555)
ss_img = ImageGrab.grab(ss_region)
ss_img.save("winn.jpg")
ssr = (731,800,818,856)
ss = ImageGrab.grab(ssr)
ss.save("winodd.jpg")
#print(pyg.position())
path_to_image = "winn.jpg"
img = Image.open(path_to_image)
text = pytesseract.image_to_string(img)
print(text)
path_to_image = "winodd.jpg"
img = Image.open(path_to_image)
text = pytesseract.image_to_string(img)
ff.write(text.split("/"))