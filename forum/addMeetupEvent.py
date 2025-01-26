######################################################
#                    Imports                         #
######################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

######################################################
#                  Variables                         #
######################################################
# Meetup username and password
username = 'ENTER EMAIL'
password = 'ENTER PASSWORD'
meetup_page = 'ENTER YOUR MEETUP PAGE HERE'
event_page = 'ENTER YOUR MEETUP EVENT PAGE HERE'
driver = webdriver.Chrome("ENTER CHROMEDRIVER PATH")
driver.get('https://www.meetup.com')

######################################################
#                  Meetup XPATHS                     #
######################################################

print("Let's Begin")
emailelement = driver.find_element(By.XPATH, ".//*[contains(@id, 'email')]").send_keys(username)
print("Username Entered")

passwordelement = driver.find_element(By.XPATH, ".//*[contains(@id, 'pass')]").send_keys(password)
print("Password Entered")

driver.find_element(By.XPATH, ".//*[contains(@id, 'loginbutton')]").click()
print("Login Successful..")

time.sleep(1)
print("Going to the Meetup page now...")
driver.get(meetup_page)

time.sleep(1)
print("Now going to the Events page")
driver.get(event_page)

print("Clicking on the Event Name field")
eventsbutton = driver.find_element(By.XPATH, './/*[@class="event-name-field"]').click()

time.sleep(2)
print("Adding event name information")
eventname = "Automated Coffee For All"
eventbutton = driver.find_element(By.XPATH, './/*[@class="event-name-input"]').send_keys(eventname)

time.sleep(2)
print("Clicking on the Description field")
descriptionname = "We are having an automation coffee blowout"
descriptionbutton = driver.find_element(By.XPATH, './/*[@class="description-field"]').click()

# Enter description info
time.sleep(2)
print("Entering Description information")
descriptionbutton = driver.find_element(By.XPATH, './/*[@class="description-input"]').send_keys(descriptionname)

# Select Category dropdown
time.sleep(2)
print("Click on the Category dropdown")
categorydropdown = driver.find_element(By.XPATH, ".//span[contains(text(), 'Select Category')]").click()

# Click on sub category dropdown
time.sleep(2)
print("Click on the Art Category from dropdown")
categorybutton = driver.find_element(By.XPATH, './/*[@class="category-option"]').click()

# Click on frequency dropdown
time.sleep(2)
print("Click on the Frequency dropdown")
frequencydropdown = driver.find_element(By.XPATH, './/*[@class="frequency-dropdown"]').click()

# Click on frequency sub dropdown
time.sleep(2)
print("Click on the Occurs Weekly from dropdown")
frequencybutton = driver.find_element(By.XPATH, ".//span[contains(text(), 'Occurs Weekly')]").click()

# Click on starts calendar
time.sleep(2)
print("Click on the Starts Calendar")
startscalendar = driver.find_element(By.XPATH, './/*[@class="starts-calendar"]').click()

time.sleep(2)
print("Click on the Start Date")
startdate = driver.find_element(By.XPATH, './/*[@class="start-date"]').click()

# Publish event
time.sleep(2)
print("Submit Event")
submitevent = driver.find_element(By.XPATH, './/*[@class="submit-event-button"]').click()
