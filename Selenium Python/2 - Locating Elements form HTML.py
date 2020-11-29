from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = 'C:\\Program Files (x86)\\Chrome Web Driver\\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

print(driver.title)

search = driver.find_element_by_name("s")
# We access the search box in the website

search.send_keys("test")
# We send(type) the value "test" inside the search box

search.send_keys(Keys.RETURN)
# Enter key is also called as return
# We press Enter key to search for the value we entered

# print(driver.page_source)
# driver.page_source returns the page_source of the page that we opened

# Now will Access more elements of the page that we opened

"""
When we move from one web page to other using Selenium and want to access the html from the latter one we need to wait for that page to properly load
"""

try:
    date = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="post-3707"]/header/div/span[1]/a/time[1]'))
    )
    print(date.text)
    time.sleep(10)

except Exception as e:
    print(e)
    driver.quit()

finally:
    driver.quit()


# time.sleep(10)

# driver.quit()

