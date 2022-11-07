import pyautogui as pyg
import time as t
import mouse as m
import keyboard
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
a=0
while keyboard.is_pressed("esc")==False:
    ff = open("data.txt", "w")
    pb=(1279,917)
    pyg.moveTo(pb)
    t.sleep(1)
    m.press()
    t.sleep(1)
    m.release()
    b = 349
    c = 383
    t.sleep(1)
    for i in range(5):

        ss_region = (182,b,253,c)
        ss_img = ImageGrab.grab(ss_region)
        ss_img.save(f"{i + 1}.jpg")
        b=b+120
        c=c+122
    t.sleep(1)
    ss_region = (182,932,253,990)
    ss_img = ImageGrab.grab(ss_region)
    ss_img.save(f"{6}.jpg")


    arr=[]
    for k in range(1,7):
        #Define path to image
        path_to_image = f'{k}.jpg'
        #Open image with PIL
        img = Image.open(path_to_image)
        #Extract text from image
        text = pytesseract.image_to_string(img)
        print(text)
        text=text.split("/")
        try:
            arr.append(int(text[0]))
        except:
            arr.append(text[0])
    max=30
    l=0
    for i in range(len(arr)):
        try:
            if arr[i][0]=="A":
                arr[i]=4
        except:
            continue
    for i in range(len(arr)):
        try:
            if arr[i][0]=="E":
                pos = i
                #if 2 in arr:
                 #   pos=int(arr.index(2))

                break
            #if arr[i][0]=="A":
             #   if 4 == max:
             #       if i < pos:
              #          pos = i
             #   elif 4 < max:
               #     max = 4
               #     pos = i
        except:
            if arr[i]==max:
                if i<pos:
                    pos=i
            elif arr[i]<max:
                l=max
                max=arr[i]
                pos=i
    #if pos==5 and arr.index(l)==2:
    #    pos=2
    ff.write(f"{arr},{pos+1}")
    dic={
        0:(182,352),
        1:(182,472),
        2:(182,593),
        3:(182,688),
        4:(182,808),
        5:(182,928)
    }
    pyg.moveTo(dic.get(pos))
    m.press()
    t.sleep(1)
    m.release()
    ssr=(1382,391,1510,431)
    ss_img = ImageGrab.grab(ssr)
    ss_img.save("bal.jpg")
    path_to_image = "bal.jpg"
    img = Image.open(path_to_image)
    bal = int(pytesseract.image_to_string(img))

    pyg.moveTo(1521,513)
    if bal<25000:
            m.press()
            t.sleep(2)
            m.release()
    elif bal>1000000:
        m.press()
        t.sleep(8)
        m.release()
    else:
            m.press()
            t.sleep(4)
            m.release()
    pyg.moveTo(1235,771)
    m.press()
    t.sleep(1)
    m.release()

    t.sleep(43)
    try:
        ssr = (731, 800, 818, 856)
        ss = ImageGrab.grab(ssr)
        ss.save("winodd.jpg")
        path_to_image = "winodd.jpg"
        img = Image.open(path_to_image)
        text = pytesseract.image_to_string(img)
        text=text.split("/")
        ff.write(text[0])
        ff.write(arr.index(text[0])+1)
        t.sleep(1)
        ff.write("\n")
    except:
        pass
    ff.close()
    m.press("right")
    t.sleep(1)
    m.release("right")

    print(a)
    #print(pyg.position())



