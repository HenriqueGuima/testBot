import project as pro
from homepage_reports import owers_report as owers
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import types
import typing
import os
import constants as const

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
pro.run(chrome)
print("### LOGIN ###")
WebDriverWait(chrome, 15).until(EC.presence_of_element_located((By.XPATH, const.USERNAME_FIELD_XPATH)))
pro.login(chrome, const.USERNAME, const.PASSWORD)
print("### HOMEPAGE ###")
owers.owers_list(chrome)
# owers.check_pagination(chrome)
owers.get_owers_name(chrome)
