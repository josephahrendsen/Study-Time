import os
import pyautogui as pag
import time

# how long to wait
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)

print('1')
# closing the tab
print("Locating Reddit")



# moving to reddit
print("Mouse Position:", pag.position())

time.sleep(3)
a = pag.locateCenterOnScreen(r"C:\Users\Helquin\PycharmProjects\GoogleCloudHackAthon\Reddit1.PNG")

print("we found reddit at", a)


#pag.hotkey('ctrl', 'w')



