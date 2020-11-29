from selenium import webdriver
import time

PATH = 'C:\\Program Files (x86)\\Chrome Web Driver\\chromedriver.exe'
driver = webdriver.Chrome(PATH)
# We want to use Chrome Web Driver and the path of the Web Driver is given

driver.get("https://techwithtim.net")
# To Open the specified Website

time.sleep(10)

# driver.close()
# Above statement will close only the Web Page/Tab


print(driver.title)
# driver.title returns the title of the Webpage that we opened

driver.quit()
# Above statement will close the entire window of the Browser