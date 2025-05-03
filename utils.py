from selenium.common import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

from config.configreader import *


def openBrowser():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no UI)
    options.add_argument("--no-sandbox")  # Required for GitHub Actions/Linux
    options.add_argument("--disable-dev-shm-usage")  # Prevents memory issues
    options.add_argument("--disable-gpu")  # Optional: GPU not needed in CI
    options.add_argument("--window-size=1920,1080")  # Ensure full page visibility

    # Use default installed chromedriver
    service = Service("/usr/bin/chromedriver")  # GitHub Actions Ubuntu path

    driver = webdriver.Chrome(service=service, options=options)
    return driver


# driver = openBrowser()

def inputDetails(driver, xpath, data):
    #driver.find_element(By.XPATH, xpath).send_keys(data)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    driver.find_element(By.XPATH, xpath).send_keys(data)
    print(data + " written...")


def clickElement(driver, xpath):
    #driver.find_element(By.XPATH, xpath).click()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    driver.find_element(By.XPATH, xpath).click()
    print("Element clicked...")


def check_ExtraQuestionTab(driver):
    try:
        element = driver.find_element(By.XPATH, get_uploadResume_xpath_value('xpath_crossClick'))
        element.click()
        print("Extra Question asking, so rejected those questions")
    except NoSuchElementException:
        print("Element not found. Exiting without action.")

