######################################################
#                    Imports                         #
######################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

######################################################
#                  Variables                         #
######################################################
# facebook username and password
username = 'ENTER EMAIL'
password = 'ENTER PASSWORD'
business_page = 'ENTER YOUR FB BUSINESS PAGE HERE'
event_page = 'ENTER YOUR FB BUSINESS EVENT PAGE HERE'
driver = webdriver.Chrome("ENTER CHROMEDRIVER PATH")
driver.get('https://www.facebook.com')



######################################################
#                  FB XPATHS                  #
######################################################

print("Let's Begin")
emailelement = driver.find_element(By.XPATH,".//*[contains(@id, 'email')]").send_keys(username)
print("Username Entered") 

passwordelement = driver.find_element(By.XPATH,".//*[contains(@id, 'pass')]").send_keys(password)
print("Password Entered") 

driver.find_element_by_id('loginbutton').click()
print("Login Successfull..")

time.sleep(1)
print("Going to the Business page now...")
driver.get(business_page)

time.sleep(1)
print("Now going to the Events page")
driver.get(event_page)

print("Clicking on the Event Name field")
eventsbutton = driver.find_element(By.XPATH,'.//*[@class="_42ft _4jy0 _3-90 _4jy4 _4jy1 selected _51sy"]').click()

time.sleep(2)
print("Adding event name information")
eventname= "Automated Coffee For All"
eventbutton = driver.find_element(By.XPATH,'.//*[@class="_1o0a _55r1 _1488 _58ak _3ct8"]').send_keys(eventname)

time.sleep(2)
print("Clicking on the Description field")
descriptionname = ("We are having an automation coffee blowout")
descriptionbutton = driver.find_element(By.XPATH,'.//*[@class="_f6a _5yk1"]').click()

# Click description field
time.sleep(2)
print("Clicking on the Description field")
descriptionname = ("We are having an automation coffee blowout")
descriptionbutton = driver.find_element(By.XPATH,'.//*[@class="_5rp7"]').click()

# Enter description info
time.sleep(2)
print("Entering Description information")
descriptionname = ("We are having an automation coffee blowout")
descriptionbutton = driver.find_element(By.XPATH,'.//*[@class="notranslate _5rpu"]').send_keys(descriptionname)

# Select Category dropdown
time.sleep(2)
print("Click on the Category dropdown")
categorydropdown = driver.find_element(By.XPATH,".//span[contains(text(), 'Select Category')]").click()

# Click on sub category dropdown
time.sleep(2)
print("Click on the Art Category from dropdown")
descriptionbutton = driver.find_element(By.XPATH,'.//*[@class="_54nh"]').click()

# Click on frequency dropdown
time.sleep(2)
print("Click on the Frequency dropdown")
descriptionbutton = driver.find_element(By.XPATH,'.//*[@class="_3r__ _2agf _4o_4 _4jy0 _4jy4 _517h _51sy _42ft _p"]').click()

# Click on frequency sub dropdown
time.sleep(2)
print("Click on the Occurs Weekly from dropdown")
frequencybutton = driver.find_element(By.XPATH,".//span[contains(text(), 'Occurs Once')]").click()

# Click on starts calendar
time.sleep(2)
print("Click on the Starts Calendar")
frequencyCalendar = driver.find_element(By.XPATH,'.//*[@class="_3smp"]').click()

time.sleep(2)
print("Click on the Start Date")
frequencyCalendarCalendarSelectDate = driver.find_element(By.XPATH,'.//*[@class="_5c66 _5hpx"]').click()

# Publish event
time.sleep(2)
print("Submit Event")
submitevent = driver.find_element(By.XPATH,'.//*[@class="_42ft _4jy0 layerConfirm _2pi9 _4jy3 _4jy1 selected _51sy"]').click()
