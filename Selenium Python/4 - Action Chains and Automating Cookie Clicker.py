from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

PATH = 'C:\\Program Files (x86)\\Chrome Web Driver\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(50)

# bigCookie - Cookie to be Clicked
# cookies - Number of Cookies
# productPrice0 - Price of Cursor
# productPrice1 - Price of Grandma

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice"+str(i)) for i in range(1, -1, -1)]

# Creating Action Chain Object
actions = ActionChains(driver)
# Action Chain Creates a Queue of Actions that we provide to its object


for i in range(1000000):
    actions.click(cookie)
    actions.perform()
    count = int(cookie_count.text.split(" ")[0].replace(",", ""))
    # print(count)
    for item in items:
        value = int(item.text)
        # print(value)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
    