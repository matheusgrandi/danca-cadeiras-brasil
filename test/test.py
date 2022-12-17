import pickle
import os
from selenium import webdriver
import time


option = webdriver.ChromeOptions()
option.add_argument("--no-sandbox")        
driver = webdriver.Chrome(options=option)
driver.get("https://google.com")
time.sleep(5)
if os.path.exists('cookies.pkl'):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    sleep(5)
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))