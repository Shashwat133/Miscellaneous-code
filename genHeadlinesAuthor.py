import cv2 
import re
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

def gen_Headline_Author(image_path, n = 4, language = "eng"):
    
    # Author extraction
    img_cv = cv2.imread(image_path)
    try:
        #img_cv = get_grayscale(img_cv)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    except:
        pass
    custom_config = r'--oem 3'
    text = pytesseract.image_to_string(img_cv, lang = language, config=custom_config)
    
    outputList = text.split('\n')
    while outputList.count('') != 0:
        outputList.remove('')
    for i in range(len(outputList)):
        if outputList[i].count('@') > 0:
            outputList[i] = outputList[i].replace(' ','')
        
    flag = False
    for i in range(len(outputList)):
        line = outputList[i]
        match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
        if len(match) != 0:
            flag = True
            author = outputList[i-1]
            break
    if not flag:
        author = "Bureau"
    
    # Headline extraction
    img_cv = cv2.imread(image_path)
    image = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    kernel = np.ones((n,n), np.uint8)  # for english 4,4 for hindi 6,6
    temp_image = cv2.dilate(image, kernel = kernel)
    
    boxes = pytesseract.image_to_data(temp_image, lang = language)
    flag1 = False
    #print(boxes)
    coordinates = list()
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12 and b[2] == '1':
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(image, (x-6,y-6), (w+x+6,h+y+6), (0,0,255), 2)
                coordinates.append((x,y,w,h))
                
    image_copy = image.copy()
    headline = ""
    try:
        for c in coordinates:
            x, y, w, h = c
            image_roi = image_copy[y-5:y + h+4.5, x-4:x + w+4] 
            text = pytesseract.image_to_string(image_roi,lang = language, config =  r'--oem 3 --psm 7') # config important otherwise accuracy low
            headline += text

        headline = headline.replace('\n\x0c',' ').strip()
    except:
        pass
    
    return headline, author
    
def thinHeadline(image_path):
    img_cv = cv2.imread(image_path)
    try:
        #img_cv = get_grayscale(img_cv)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    except:
        pass
    
    custom_config = r'--oem 3'
    text = pytesseract.image_to_string(img_cv, config=custom_config)
    
    outputList = text.split('\n\n')
    while outputList.count('') != 0:
        outputList.remove('')

    headline = outputList[1]
    headline = headline.replace('\n',' ')
    
    return headline
    
def getHeadlineutil(image_path):
    x = ''
    n = 4
    x, y = gen_Headline_Author(image_path, n = n)
    if x == '':
        n = 7
        x, y = gen_Headline_Author(image_path, n = n)
    if x == '':
        x = thinHeadline(image_path)
    return x, y

headline, author = getHeadlineutil("2b2ec4_179296_5.jpg")        