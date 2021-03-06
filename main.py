from PIL import ImageGrab
import numpy as np 
import time
import pyautogui

class Box:
    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.type = kind

def plzDontJudgeMyFunctionNames(i,arr):
    result = np.where(arr == str(i))
    print(result)
    cords = list(zip(result[0], result[1]))
    return cords

def checkSurrounding(x,y,arr):
    boxes = []
    count = [0] * 8
    indices = [(x+1, y), (x-1, y), (x, y+1), (x, y-1),
               (x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]
    for i in indices:
        if(i[1] > -1 and i[1] < 10 and i[0] > -1 and i[0] < 8):
            if(arr[i] == 'green'):
                count[0] += 1
                boxes.append(Box(i[1], i[0],arr[i]))
            elif(arr[i] == str(1)):
                count[1] += 1
                boxes.append(Box(i[1], i[0], arr[i]))
            elif(arr[i] == str(2)):
                count[2] += 1
                boxes.append(Box(i[1], i[0], arr[i]))
            elif(arr[i] == str(3)):
                count[3] += 1
                boxes.append(Box(i[1], i[0], arr[i]))
            elif(arr[i] == str(4)):
                count[4] += 1
                boxes.append(Box(i[1], i[0], arr[i]))
            elif(arr[i] == str(5)):
                count[5] += 1
                boxes.append(Box(i[1], i[0], arr[i]))
            elif(arr[i] == 'null'):
                count[6] += 1
                boxes.append(Box(i[1], i[0], arr[i]))
            elif(arr[i] == 'flag'):
                count[7] += 1
                boxes.append(Box(i[1], i[0], arr[i]))
        else:
            continue
    
    return count, boxes

def markFlag(count,boxes,arr,x,y):
    for i in range(1,6):
        if (arr[x, y] == str(i) and count[0] + count[7] == i):
            for box in boxes:
                if(box.type == 'green'):
                    print("Flag")
                    print(box.x, box.y)
                    flag(box.x, box.y)

def safeClick(count, arr, x, y):
    for i in range(1, 6):
        if (arr[x, y] == str(i) and count[7] == i and count[0] > 0):
            print("Click")
            print(y, x)
            doubleClick(y,x)

def click(i,j):
    x = 671+(i*62)
    y = 429+(j*62)
    pyautogui.click(x,y)

def flag(i, j):
    x = 671+(i*62)
    y = 429+(j*62)
    pyautogui.click(x, y, button='right')

def doubleClick(i,j):
    x = 671+(i*62)
    y = 429+(j*62)
    pyautogui.mouseDown(x,y)
    pyautogui.mouseDown(x,y,button='right')
    pyautogui.mouseUp(x, y)
    pyautogui.mouseUp(x, y,button='right')


def tellMeWhatThisIs(arg):
    arr = arg[31, :]

    one = np.array([25, 118, 210])
    # two = np.array([67, 144, 66])
    three = np.array([211, 47, 47])
    four = np.array([123, 31, 162])
    five = np.array([255, 143, 0])
    flag = np.array([230, 51, 7])
    green = np.array([162, 209, 73])
    green2 = np.array([170, 215, 81])
    white = np.array([215, 184, 153])
    white2 = np.array([229, 194, 159])

    mid = arr[20:35]

    if(np.all(mid == green) or np.all(mid == green2)):
        return "green"
    elif(np.all(mid == white) or np.all(mid == white2)):
        return "null"
    else:
        for color in arr:
            if(np.array_equal(color, one)):
                return 1
            elif(np.array_equal(color, three)):
                return 3
            elif(np.array_equal(color, four)):
                return 4
            elif(np.array_equal(color, five)):
                return 5
            elif(np.array_equal(color, flag)):
                return "flag"


def seeWhatsHapping(cords, square_side, x, y):
    mat = []
    img = np.array(ImageGrab.grab(bbox=cords))
    for i in range(0, y, square_side):
        temp = []
        for j in range(0, x, square_side):
            crop_img = img[i:i+square_side, j:j+square_side]
            img_arr = np.array(crop_img)
            app = tellMeWhatThisIs(img_arr)
            if app is None:
                temp.append(2)
            else:
                temp.append(app)
        mat.append(temp)

    mat = np.array(mat)
    return mat



difficulty = 1

if(difficulty == 1):
    square_side = 62
    x = square_side * 10
    y = square_side * 8
    game_cords = (640, 400, 640+x, 400+y)
    X_pos = 671
    Y_pos = 429

easy = [10,8]

# output = seeWhatsHapping(game_cords,square_side,x,y)
# print(output[3][6])

time.sleep(1)
click(4,4)
for loop in range(15):
    output = seeWhatsHapping(game_cords, square_side, x, y)
    for numbers in range(1,6):
        cords1 = plzDontJudgeMyFunctionNames(numbers,output)
        for cords in cords1:
            output = seeWhatsHapping(game_cords, square_side, x, y)
            surr = checkSurrounding(cords[0],cords[1],output)
            markFlag(surr[0], surr[1], output, cords[0], cords[1])
    for numbers in range(1, 6):
        cords1 = plzDontJudgeMyFunctionNames(numbers, output)
        for cords in cords1:
            output = seeWhatsHapping(game_cords, square_side, x, y)
            surr = checkSurrounding(cords[0], cords[1], output)
            safeClick(surr[0], output, cords[0], cords[1])







# image = cv2.imread(".\\test images\\CAPTURE.PNG")  
# template = cv2.imread(".\\Templates\\one.PNG")  

