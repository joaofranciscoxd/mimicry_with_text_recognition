import time
import pyautogui
import keyboard
import pytesseract as pyt
import numpy as np
from PIL import ImageGrab
import cv2

pyt.pytesseract.tesseract_cmd = (r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe')
pos = list()
gravando = False
reproduzindo = False
if __name__ == '__main__':
    while True:
        if keyboard.is_pressed('c'):
            print("Gravação começou")
            time.sleep(0.25)
            gravando = True
        if keyboard.is_pressed('f'):
            print("Gravação finalizada")
            time.sleep(0.25)
            gravando = False
        if keyboard.is_pressed('r'):
            print("Reproduzindo gravação")
            time.sleep(0.25)
            reproduzindo = True
        if keyboard.is_pressed('p'):
            print("Parando gravação")
            time.sleep(0.25)
            reproduzindo = False
        if keyboard.is_pressed('l'):
            print("Limpou!")
            time.sleep(0.25)
            pos = list()

        if keyboard.is_pressed('esc'):
            print("Saindo...")
            time.sleep(0.25)
            break
        if gravando == True and reproduzindo ==False:
            click = False
            time.sleep(0.09)
            #Captura posições do mouse
            currentMouseX, currentMouseY = pyautogui.position()
            # Captura status de clique do mouse
            if keyboard.is_pressed('q'):
                print("CLICK!")
                click = True
                time.sleep(0.25)
            pos.append([currentMouseX, currentMouseY,click])
            #print(pos)
        if reproduzindo == True and gravando == False :
            if len(pos) == 0:
                print("Não há mais comandos gravados!!")
                reproduzindo = False
            else:
                if len(pos)==0:
                    reproduzindo = False
                    break
                if pos[0][2] == True:
                    pyautogui.click(pos[0][0], pos[0][1])
                    screen = np.array(ImageGrab.grab(bbox=(230, 180, 580, 223)))
                    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
                    screen_gray = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
                    (thresh, screen_gray_bin) = cv2.threshold(screen_gray, 55, 255, cv2.THRESH_BINARY)
                    cv2.moveWindow("Tela", 920 ,0)
                    cv2.imshow('Tela', screen_gray_bin)
                    cv2.waitKey(1)
                    text = pyt.image_to_string(screen_gray_bin, lang='por', config=' --psm 13 ')
                    print("TEXTO RECONHECIDO:")
                    print(text[:-1])
                else:
                    pyautogui.moveTo(pos[0][0],pos[0][0])
                pos.pop(0)
                #print(pos)
    cv2.destroyAllWindows()




