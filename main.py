#Importing Seleniam and Webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
#Initializing the Safari Webdriver
driver = webdriver.Safari()

#open a website
driver.get("https://en.wikipedia.org/wiki/Apple_Inc.")

#find an element on the webpage
main_content = driver.find_element(By.ID, "mw-content-text")

#print the text of the found element
print(main_content.text)

driver.quit()
