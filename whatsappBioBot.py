# Use Selenium to automatically update the Whatsapp Bio

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException


driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
while True:
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,'//span[@data-icon="default-user"]/../..'))
        )
        break
    except TimeoutException:
        input("Whatsapp did not load yet. Press enter to retry")

sleep(1)

def resetPage(times=10):
    for i in range(times):
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

def updateBio(text):
    try:
        resetPage()

        # click profile
        driver.find_element(By.XPATH,'//span[@data-icon="default-user"]/../..').click()

        # click pencil
        driver.find_element(By.XPATH,'//button[@title="Click to edit About"]').click()

        # click textbox
        driver.find_element(By.XPATH,'//div[@contenteditable="true"]').click()

        # selects all
        driver.find_element(By.XPATH,'//div[@contenteditable="true"]').send_keys(Keys.CONTROL,"a")

        # input text
        driver.find_element(By.XPATH,'//div[@contenteditable="true"]').send_keys(text)
        
        # click done
        driver.find_element(By.XPATH,'//button[@title="Click to save, ESC to cancel"]').click()

        resetPage()
        return True
    except:
        resetPage(25)
        print("update fail, retry")
        updateBio(text)