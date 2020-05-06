import pyautogui
from PIL import Image, ImageGrab
import time
#from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)
    return

#def draw():
def isCollide(data):
    #for the birds
    for i in range(300, 415):
        for j in range(410, 567):
            if data[i, j]<100:
                hit('down')
                return


    #for the cactus
    for i in range(180, 355):
        for j in range(567, 650):
            if data[i,j]<100:
                hit('up')
                return
    return

if __name__ == '__main__':
    print("hey ..about in 3 sec")
    time.sleep(3)

    while True:

        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)


