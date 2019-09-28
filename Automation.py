import pyautogui as pag
import time
import pyperclip

# while loop to check each tab
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
pag.hotkey('alt', 'tab')
#finding out first tab that isn't NSFW
firstUrl =""
a = 0
while a == 0:


    pag.hotkey('ctrl', 'e')
    time.sleep(.2)
    pag.hotkey('ctrl', 'z')
    time.sleep(.2)
    pag.hotkey('ctrl', 'a')
    time.sleep(.2)
    pag.hotkey('ctrl', 'c')

    firstUrl = pyperclip.paste()
    print(firstUrl)
    if "facebook.com" in firstUrl or"youtube" in firstUrl or "twitter" in firstUrl or "reddit" in firstUrl or "imgur" in firstUrl or "tumblr" in firstUrl or "coolmathgames" in firstUrl or "poptropica" in firstUrl:
        pag.hotkey("ctrl","w")

    else:
        firstUrl = pyperclip.paste()
        print("Your first URL string is: " + firstUrl)
        a = 1




urlList = [1]
i = 0
while firstUrl != urlList[i]:
    # move up the tabs
    #Debug
    #print(firstUrl)
    pag.hotkey('ctrl', 'pageup')

    # takes the URL of that Tab
    pag.hotkey('ctrl', 'e')
    time.sleep(.4)
    pag.hotkey('ctrl', 'z')
    time.sleep(.4)
    pag.hotkey('ctrl', 'a')
    time.sleep(.4)
    pag.hotkey('ctrl', 'c')
    urlList.append(pyperclip.paste())
    compare = str(urlList[i+1])

    #for Debugging
    #print(compare)


    # check if it is one of our NSFW sites
    if "facebook" in compare:
        pag.hotkey("ctrl","w")
    if "youtube" in compare:
        pag.hotkey("ctrl","w")
    if "tumblr" in compare:
        pag.hotkey("ctrl","w")
    if "reddit" in compare:
        pag.hotkey("ctrl","w")
    if "coolmathgames" in compare:
        pag.hotkey("ctrl","w")
    if "imgur" in compare:
        pag.hotkey("ctrl","w")
    if "poptropica" in compare:
        pag.hotkey("ctrl","w")
    if "twitter" in compare:
        pag.hotkey("ctrl","w")




    i = i + 1


print (urlList)
