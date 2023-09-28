import time
import constants as const
from selenium.webdriver.common.by import By


def run(chrome):
    print('Starting in {}'.format(const.BASE_URL))
    chrome.get(const.BASE_URL)
    chrome.maximize_window()    

def login(chrome, username, password):
    print('Login...')
    find_user = chrome.find_element(By.XPATH, const.USERNAME_FIELD_XPATH)
    find_password = chrome.find_element(By.XPATH, const.PASSWORD_FIELD_XPATH)
    find_login_button = chrome.find_element(By.XPATH, const.LOGIN_BUTTON_XPATH)
    find_user.send_keys(username)
    find_password.send_keys(password)
    print('Loggin in with {}'.format(const.USERNAME))
    time.sleep(1)
    find_login_button.click()
