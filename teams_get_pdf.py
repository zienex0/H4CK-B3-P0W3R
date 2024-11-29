from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
def click_element(driver,xpath:str):
    try:
        temp = driver.find_element(By.XPATH, xpath)
        temp.click()
        time.sleep(12)
    except NoSuchElementException:
        print(f"Element with XPath '{xpath}' not found.")
    except ElementClickInterceptedException:
        print(f"Element with XPath '{xpath}' not found.")

def set_slider_to_max(driver, slider_xpath: str):
    try:
        slider = driver.find_element(By.XPATH, slider_xpath)
        #  JavaScript to set the slider value to its maximum
        max_value = slider.get_attribute("max")
        driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));",
            slider, max_value
        )
        time.sleep(8)  
        print(f"Slider set to maximum value: {max_value}")
    except NoSuchElementException:
        print(f"Slider with XPath '{slider_xpath}' not found.")

def getPdf(driver):
    # Load PPJ Page
    teams_ppj_xpath = '//div[@data-tid="19:5FW7_kkzi7ae7mfYx6FZiKt77mdA696z7PLK_QHrFx01@thread.tacv2-team-card"]'
    click_element(driver,teams_ppj_xpath)

    # Load files Page of PPJ
    teams_ppj_files_xpath = "//button[@id='3ed5b337-c2c9-4d5d-b7b4-84ff09a8fc1c']"
    click_element(driver,teams_ppj_files_xpath)
    # Open filters
    ppj_files_filters_xpath = "//div[@class='ms-OverflowSet-item item-104']"   # Element with XPath '//div[@class='ms-OverflowSet-item item-104']' not found. Why??????
    click_element(driver,ppj_files_filters_xpath)
    
    # Set slider to maximum
    slider_xpath = '//input[@id="slider-162"]'
    set_slider_to_max(driver, slider_xpath)




