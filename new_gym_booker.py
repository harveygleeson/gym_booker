from datetime import datetime
from threading import Timer
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import settings

#from os import environ

# Set gym slot, student number, time
slot = settings.slot
student_number = settings.studentnumber
hour = settings.hour
minute = settings.min

# Time settings
today=datetime.today()

# Set time for program to run here (24 hr)
y = today.replace(day=today.day, hour=hour, minute=minute, second=57, microsecond=0)

delta_t=y-today
secs=delta_t.seconds+1

print(f"Booking Gym at {hour}:{minute} for {hour + 3}:{minute + 1} for {student_number}")

def book_gym():

    # For chrome
    browser = webdriver.Chrome('/Users/harveygleeson/Documents/Coding/Python/Gym Booker Bot/chromedriver')

    # Gym booking url
    browser.get("https://hub.ucd.ie/usis/W_HU_MENU.P_PUBLISH?p_tag=GYMBOOK")

    done = False

    while not done:

        try:
            # Click on button for booking 
            # (change the number between | and " to change the time of slot)
            print("Trying to click on slot")
            browser.find_element_by_xpath(f'//*[@id="SW300-1|{slot}"]/td[6]/a').click()
            print("Clicked on slot")

            # Click on accept cookies
            sleep(1)
            print("Trying to click on accept cookies")
            browser.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
            print("Clicked on accept cookies")

            # Enter UCD number
            print("Trying to input student number")
            browser.find_element_by_xpath('//*[@id="single-column-content"]/div/div/div/div[2]/div/form/input[4]').send_keys(student_number, Keys.RETURN)
            print("Just input student number and pressed return")

            # Click on confirm booking
            sleep(0.5)
            print("Trying to click on confirm booking")
            browser.find_element_by_xpath('//*[@id="single-column-content"]/div/div/div/div[2]/div/a[1]').click()
            print("Clicked on confirm booking")

            done = True


        except:
            print("Something went wrong")
            sleep(.5)
            browser.refresh()
            print("Refreshed the page")

    # Wait 10 seconds and close
    print("Booked successfully")
    sleep(10)
    browser.quit()


t = Timer(secs, book_gym)
t.start()