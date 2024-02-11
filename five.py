#https://selenium-python.readthedocs.io/navigating.html <-- Official Documentation
# this provides all the webdriver implementations
from selenium import webdriver
#The KEYS class provides keys in teh keyboard like RETURN, F1, ALT.
from selenium.webdriver.common.keys import Keys
#the BY class is used to locate elements within a document
from selenium.webdriver.common.by import By
#import time finction
import time

#Next we have to implement the instance of Chrome Webdriver
driver = webdriver.Chrome()



#the driver.get method will navigate to a webpage by the URL

driver.get("http://www.python.org")
time.wait(25)
driver.quit()
