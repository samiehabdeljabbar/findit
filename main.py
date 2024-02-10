#Importing Seleniam and Webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
#Initializing the Safari Webdriver
driver = webdriver.Safari()

#open a website
driver.get("https://en.wikipedia.org/wiki/Apple_Inc.")

#find an element on the webpage
element = driver.find_element(By.CSS_SELECTOR, 'apple')

#print the text of the found element
print(element.text)

driver.quit()
