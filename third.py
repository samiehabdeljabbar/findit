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

driver.get("https://www.reddit.com/new/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"overflow-x-hidden xs:overflow-visible v2 pt-[var(--page-y-padding)]"))
)

time.sleep(25)
driver.quit()
