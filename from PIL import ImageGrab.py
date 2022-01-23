from PIL import ImageGrab
import cv2  
import numpy as np 
import time
import os

os.chdir(".\\test images")

def tellMeWhatThisIs(arg):
    arr = arg[31, :]

    one = np.array([25, 118, 210])
    two = np.array([67, 144, 66])
    three = np.array([211, 47, 47])
    four = np.array([123, 31, 162])
    flag = np.array([230, 51, 7])
    green = np.array([162, 209, 73])
    white = np.array([215, 184, 153])

    mid = arr[20:35]

    if(np.all(mid == green)):
        return 6
    elif(np.all(mid == white)):
        return 7
    else:
        for color in arr:
            if(np.array_equal(color, one)):
                return 1
            elif(np.array_equal(color, two)):
                return 2
            elif(np.array_equal(color, three)):
                return 3
            elif(np.array_equal(color, four)):
                return 4
            elif(np.array_equal(color, flag)):
                return 5


def seeWhatsHapping(cords, square_side, x, y):
    mat = []
    img = np.array(ImageGrab.grab(bbox=cords))
    for i in range(0, y, square_side):
        temp = []
        for j in range(0, x, square_side):
            filename = str(i) + str(j) + ".PNG"
            print(filename)
            crop_img = img[i:i+square_side, j:j+square_side]
            crop_img = np.array(crop_img)
            cv2.imwrite(filename, crop_img)
    return mat



difficulty = 1

if(difficulty == 1):
    square_side = 62
    x = square_side * 10
    y = square_side * 8
    game_cords = (640, 400, 640+x, 400+y)

easy = [10,8]

time.sleep(3)

output = seeWhatsHapping(game_cords,square_side,x,y)
print(output)

# image = cv2.imread(".\\test images\\CAPTURE.PNG")  
# template = cv2.imread(".\\Templates\\one.PNG")  

