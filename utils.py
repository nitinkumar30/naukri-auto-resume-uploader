from selenium.common import NoSuchElementException

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

from config.configreader import *


def openBrowser():
    option = Options()
    option.add_argument('--headless')
    # driver = webdriver.Chrome(options=option)
    driver = webdriver.Chrome()
    return driver


# driver = openBrowser()

def inputDetails(driver, xpath, data):
    driver.find_element(By.XPATH, xpath).send_keys(data)
    print(data + " written...")


def clickElement(driver, xpath):
    driver.find_element(By.XPATH, xpath).click()
    print("Element clicked...")


def check_ExtraQuestionTab(driver):
    try:
        element = driver.find_element(By.XPATH, get_uploadResume_xpath_value('xpath_crossClick'))
        element.click()
        print("Extra Question asking, so rejected those questions")
    except NoSuchElementException:
        print("Element not found. Exiting without action.")

