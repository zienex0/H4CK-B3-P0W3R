from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

def loginToTeams(driver: webdriver, email: str, password: str, stay_open=True): 
    # ugly code, awfull xpath patterns but for now it doesnt matter. we will fix it

    driver.get("https://www.microsoft.com/pl-pl/microsoft-teams/log-in")
    time.sleep(5)
    homePageLoginButton = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/main/div/div/div/div[2]/section/div/div[2]/div/div/div/div/div/div[3]/a[1]")
    homePageLoginButton.click()

    # login tab
    time.sleep(10)

    # switch to current tab
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    _loginInp = driver.find_element(By.NAME, 'loginfmt')
    _loginInp.send_keys(email)
    _loginInp.send_keys(Keys.ENTER)

    time.sleep(8)

    # school login
    _passwd = driver.find_element(By.NAME, 'Password')
    _passwd.send_keys(password)
    _passwd.send_keys(Keys.ENTER)

    time.sleep(5)


    _dontShowAgain = driver.find_element(By.NAME, 'DontShowAgain')
    _dontShowAgain.click()


    _submit = driver.find_element(By.XPATH, '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input')
    _submit.click()
    if stay_open:
        input('Press any key to proceed...')

