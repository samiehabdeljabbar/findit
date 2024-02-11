#Following tech with tims course
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
    options=options)

driver.get("https://www.google.com/")


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.clear()
input_element.send_keys("tech with tim" + Keys.ENTER)

link = driver.find_element(By.PARTIAL_LINK_TEXT,"Tech With Tim")
link.click()

#time will make it go to sleep
time.sleep(10)

driver.quit()
