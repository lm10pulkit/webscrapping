from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()


driver = webdriver.Chrome(executable_path="C:/webdrivers/chromedriver.exe",  chrome_options=option)

driver.get("http://econpy.pythonanywhere.com/ex/001.html")

# Extract lists of "buyers" and "prices" based on xpath.
buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')



num_page_items = len(buyers)
for i in range(num_page_items):
    print(buyers[i].text + " : " + prices[i].text)

# Clean up (close browser once completed task).
driver.close()