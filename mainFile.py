from utils import *
import os

# NAUKRIUSERNAME = os.getenv("NAUKRIUSERNAME")
# NAUKRIPASSWORD = os.getenv("NAUKRIPASSWORD")

NAUKRIUSERNAME, NAUKRIPASSWORD = load_credentials()

driver = openBrowser()

driver.get(get_property_value('URL'))
driver.implicitly_wait(10)

inputDetails(driver, get_loginPage_xpath_value('xpath_username'), NAUKRIUSERNAME)
inputDetails(driver, get_loginPage_xpath_value('xpath_password'), NAUKRIPASSWORD)
clickElement(driver, get_loginPage_xpath_value('xpath_loginBtn'))

driver.implicitly_wait(20)
print("Waited for 20 secs...")

check_ExtraQuestionTab(driver)

clickElement(driver, get_uploadResume_xpath_value('xpath_profileBtn'))
driver.implicitly_wait(10)

# Extra Question Tab
check_ExtraQuestionTab(driver)

inputDetails(driver, get_uploadResume_xpath_value('xpath_resumeUpload'), 'Nitin_Resume.pdf')

driver.implicitly_wait(10)
driver.quit()
