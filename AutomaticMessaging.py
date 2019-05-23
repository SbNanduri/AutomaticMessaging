from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome() # Initializes the chrome browser

driver.get('https://www.messenger.com/')

email = driver.find_element_by_id("email")  # Finds the email field
password = driver.find_element_by_id("pass")    # Finds the password field

email.send_keys('fake_email@fake.com')
password.send_keys('hunter2')

password.send_keys(Keys.ENTER)  # Presses enter so you can be logged in

contact_name = "Contact"    # The contact you want to send the message to
contacts = driver.find_elements_by_class_name('_3oh-')

if not contact_name in contacts[0].text:
	# If the contact is not already chosen, it will be found and clicked on
	contact = driver.find_element_by_partial_link_text(contact_name)
	contact.click()

time.sleep(3)   # Gives some time for the browser to load

# Pastes the contents of the clipboard and sends it to the contact
ActionChains(driver) \
	.key_down(Keys.LEFT_CONTROL) \
	.send_keys('v') \
	.key_up(Keys.LEFT_CONTROL) \
	.key_down(Keys.ENTER) \
	.key_up(Keys.ENTER) \
	.perform()