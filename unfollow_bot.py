import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initializing the headless chrome
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("https://github.com/login")
wait = WebDriverWait(driver, 10)

# Locating username and password field
username = wait.until(EC.presence_of_element_located((By.ID, "login_field")))
password = wait.until(EC.presence_of_element_located((By.ID, "password")))

# password and username need to go into these values
username.send_keys("username/email")
password.send_keys("password")

# Clicking the sign in button
login_form = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Sign in']")))
login_form.click()

#own username
nameOfUser = "username" # Input github username here

# iterate through all pages 
for page in range(1, 50):

	#get following users list (page)
	driver.get("https://github.com/{}?page={}&tab=following".format(nameOfUser, page))
	time.sleep(3)

	# unfollow all users
	follow_button = driver.find_elements_by_xpath("//input[@aria-label='Unfollow this person']")
	try:
	    for i in follow_button:
	        i.submit()
	except:
	    pass




