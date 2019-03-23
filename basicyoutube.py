from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="C:/webdrivers/chromedriver.exe",  chrome_options=option)

driver.get("https://www.youtube.com/channel/UCHmk8iNJHvf5mGN6_pkPc7g")

chalbandkar = driver.find_elements_by_xpath('//span[@class="title style-scope ytd-mini-channel-renderer"]')

for x in chalbandkar:
	print(x)

titles = [x.text for x in chalbandkar]
count=0
for i in titles:
	count=count+1
	print(str(count)+" "+str(i))


