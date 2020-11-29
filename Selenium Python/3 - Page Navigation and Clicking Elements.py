from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = 'C:\\Program Files (x86)\\Chrome Web Driver\\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

# link = driver.find_element_by_link_text("Python Programming")
# link.click()
try:
    link1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Python Programming'))
    )
    link1.click()

    link2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-item-511"]/a'))
    )
    link2.click()

    button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="sow-button-19310003"]'))
    )
    button.click()

    driver.back()
    driver.back()
    driver.back()

    driver.forward()
    driver.forward()


except Exception as e:
    print(e)
    

# finally:
#     driver.quit()

"""

NOTE:-
Suppose we want to enter a value in a textfield or input field in a website.
So, we will first need to clear the textfield(or whatever) before entering the value that we want inside it
Hence, the code to clear the vale is:-

element.clear()

Where,  element is the variable that we used to access the variable.

"""