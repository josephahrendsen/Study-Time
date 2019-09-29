import pyautogui as pag
import time
import pyperclip
import datetime
import tkinter as tk
from tkinter import messagebox


#Asking User for input
print("Experts recommend that you take 15 minute for each study session, but you do you.")
print("")
timeToStudy = input("Hello! When would you like to end your study session?(Enter in terms of mins): ")
print("Should be string")
print(type(timeToStudy))
print("No .0 min: ")
timeToStudy = timeToStudy.replace(".0 min","")
print(timeToStudy)
print(type(timeToStudy))

timeToStudy=int(timeToStudy)
print(type(timeToStudy))

input("STOP HAMMER TIME")
#how often do we need to check the user?
severityLevel = input("How often should we check on you? (Severe, Moderate, Chill): ")



#we won't have to look for capilitization
severityLevel = severityLevel.upper()

#Take out any floating spaces.
severityLevel = severityLevel.strip()


#integer of the severity
severityLevelInt = 0
#switch statement for the severity

if severityLevel == "SEVERE":
    severityLevelInt = 1
if severityLevel == "MODERATE":
    severityLevelInt = 2
if severityLevel == "CHILL":
    severityLevelInt = 3




## POUNDPOUND ARE DEBUG COMMENTS

# This the start when the application Starts

print("The Current time and date is: ")
StartTime = datetime.datetime.now()
##DEBUG
print(StartTime)
##time.sleep(3)

# Turns it in to a string
StartTimeString = StartTime.strftime('%H,%M')
StartTimeString = int(StartTimeString.replace(',', ''))
# It should print out HH,MM
print("Our start time is: ")
print(StartTimeString)
# Replaces the Comma with a space. Also making it an int to compare it
##StartTimeString = int(StartTimeString.replace(',', ''))
# Print the fruits of our labor

#Getting the Mins from the starting time
StartTimeStringMin = int(StartTime.strftime('%M'))

#Add it to how long the user wants to study

#add this to the current time
StartTimeStringMin = StartTimeStringMin+timeToStudy

#take the current hour
StarTimeStringHour = int(StartTime.strftime("%H"))

#if it is over the 60 mark add it to hour
while StartTimeStringMin>60:
    StartTimeStringMin = StartTimeStringMin-60

    StarTimeStringHour = StarTimeStringHour+1


#The year the user is in
year1 = int(datetime.datetime.now().strftime("%Y"))

#The month the user is in
month1 = int(datetime.datetime.now().strftime("%m"))

#The day it is
day1 = int(datetime.datetime.now().strftime("%d"))




# setting end time
endTime = datetime.datetime(year1,month1, day1, StarTimeStringHour,StartTimeStringMin)

# changing the format
endTimeString = endTime.strftime('%H,%M')
# make it an int to compare it
endTimeInt = int(endTimeString.replace(',', ''))

#Take the current time again
#Make them mesurable ints
CurrentTime = (datetime.datetime.now().strftime("%H,%M"))
#make it a proper int
CurrentTimeInt = int(CurrentTime.replace(',',''))

print("the end time will be at: ", endTimeInt)
print("The current time is: ", CurrentTimeInt)


while endTimeInt > CurrentTimeInt:
    ##    time.sleep(1)
    ##    print(CurrentTimeInt)
    ##    #keep Track of the current time
    ##    CurrentTime = datetime.datetime.now()
    ##    #Change the format
    ##    CurrentTime=CurrentTime.strftime('%H,%M')
    ##    #turn it into an int
    ##    CurrentTimeInt = int(CurrentTime.replace(',', ''))

##    print(CurrentTimeInt)
    #every five min
    if severityLevelInt == 1:
        severityLevelIntSec= (300)
    #every 10 mins
    if severityLevelInt == 2:
        severityLevelIntSec = (600)
    if severityLevelInt ==3:
        severityLevelIntSec= (1200)



    time.sleep(severityLevelIntSec)
    messagebox.showinfo("CHECKUP BUTTERCUP", "go to chrome, then click okay.")
    time.sleep(.3)
    pag.hotkey('alt','tab')
    time.sleep(.3)
    firstUrl = ""
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
        if "facebook.com" in firstUrl or "youtube" in firstUrl or "twitter" in firstUrl or "reddit" in firstUrl or "imgur" in firstUrl or "tumblr" in firstUrl or "coolmathgames" in firstUrl or "poptropica" in firstUrl:
            pag.hotkey("ctrl", "w")

        else:
            firstUrl = pyperclip.paste()
            print(firstUrl)
            a = 1

    urlList = [1]
    i = 0
    while firstUrl != urlList[i]:
        # move up the tabs
        # Debug
        # print(firstUrl)
        time.sleep(.6)
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
        compare = str(urlList[i + 1])

        # for Debugging
        # print(compare)

        # check if it is one of our NSFW sites
        if "facebook" in compare:
            pag.hotkey("ctrl", "w")
        if "youtube" in compare:
            pag.hotkey("ctrl", "w")
        if "tumblr" in compare:
            pag.hotkey("ctrl", "w")
        if "reddit" in compare:
            pag.hotkey("ctrl", "w")
        if "coolmathgames" in compare:
            pag.hotkey("ctrl", "w")
        if "imgur" in compare:
            pag.hotkey("ctrl", "w")
        if "poptropica" in compare:
            pag.hotkey("ctrl", "w")
        if "twitter" in compare:
            pag.hotkey("ctrl", "w")

        i = i + 1
    message22 = ("We will check on you in another ", severityLevelIntSec, " Seconds")
    messagebox.showwarning("Lets ace this thing",message22)














#Setting it up to work between hours








# while loop to check each tab
##DEBUG
##print('4')
##time.sleep(1)
##print('3')
##time.sleep(1)
##print('2')
##time.sleep(1)
##print('1')
##time.sleep(1)

##pag.hotkey('alt', 'tab')
#finding out first tab that isn't NSFW
#firstUrl =""
#a = 0
#while a == 0:


  #  pag.hotkey('ctrl', 'e')
 #   time.sleep(.2)
   # pag.hotkey('ctrl', 'z')
    #time.sleep(.2)
    #pag.hotkey('ctrl', 'a')
#    time.sleep(.2)
 #   pag.hotkey('ctrl', 'c')

  #  firstUrl = pyperclip.paste()
#    print(firstUrl)
   # if "facebook.com" in firstUrl or"youtube" in firstUrl or "twitter" in firstUrl or "reddit" in firstUrl or "imgur" in firstUrl or "tumblr" in firstUrl or "coolmathgames" in firstUrl or "poptropica" in firstUrl:
  #      pag.hotkey("ctrl","w")

 #   else:
  #      firstUrl = pyperclip.paste()
  #      print(firstUrl)
  #      a = 1




#urlList = [1]
#i = 0
#while firstUrl != urlList[i]:
    # move up the tabs
    #Debug
    #print(firstUrl)
 #   time.sleep(.6)
  #  pag.hotkey('ctrl', 'pageup')

    # takes the URL of that Tab
   # pag.hotkey('ctrl', 'e')
    #time.sleep(.4)
   # pag.hotkey('ctrl', 'z')
   # time.sleep(.4)
   # pag.hotkey('ctrl', 'a')
   # time.sleep(.4)
    #pag.hotkey('ctrl', 'c')
    #urlList.append(pyperclip.paste())
    #compare = str(urlList[i+1])

    #for Debugging
    #print(compare)


    # check if it is one of our NSFW sites
    #if "facebook" in compare:
    #    pag.hotkey("ctrl","w")
    #if "youtube" in compare:
     #   pag.hotkey("ctrl","w")
   # if "tumblr" in compare:
   #     pag.hotkey("ctrl","w")
    #if "reddit" in compare:
    #    pag.hotkey("ctrl","w")
    #if "coolmathgames" in compare:
    #    pag.hotkey("ctrl","w")
    #if "imgur" in compare:
    #    pag.hotkey("ctrl","w")
    #if "poptropica" in compare:
    #    pag.hotkey("ctrl","w")
    #if "twitter" in compare:
    #    pag.hotkey("ctrl","w")




    #i = i + 1


#print (urlList)
