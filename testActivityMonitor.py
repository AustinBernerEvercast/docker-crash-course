import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.mac import Mac2Options
from appium.webdriver.common.appiumby import AppiumBy

def get_element(driver, xpath, t):
    """This functions takes XPATH as input and returns element once it is found
    and waits for  t seconds before giving any error."""
    element_found = None
    while t > 0:
        try:
            element_found = driver.find_element(by=AppiumBy.XPATH, value=xpath)
            if element_found != "":
                break
        except:
            time.sleep(1)
        t -= 1
    return element_found

options = Mac2Options()
options.bundle_id = "com.apple.ActivityMonitor"

appium_service = AppiumService()
appium_service.start()

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeSearchField[@elementType="45"]').send_keys("node")

# Here using get_element function because process list takes time to get loaded.
get_element(driver, '//XCUIElementTypeStaticText[@value=" node"]', 10).click()

driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@label="Inspector"]').click()

driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeTab[@title="Open Files and Ports"]').click()

driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@identifier="_XCUI:CloseWindow"]').click()

appium_service.stop()
# The wait here is needed for Mac to come out of Automation mode.
time.sleep(2)