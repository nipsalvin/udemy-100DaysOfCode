from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'

# chrome_driver_path = 'C:/Users/Nips/Desktop/Softwares/chromedriver-win64/chromedriver.exe'
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get(url)

# title = driver.title
# price= driver.find_element(By.CLASS_NAME, 'a-offscreen')
# print(title)
# print(f"Price: {price.get_attribute('innerHTML')}")

# # driver.close() #closes tab
# driver.quit() #closes browser

url2 = 'https://www.python.org/'

driver_2 = webdriver.Chrome()
driver_2.get(url2)

search_bar = driver_2.find_element(By.NAME, 'q') # Gets element that has name 'q'
print(f"Search bar is : {search_bar.get_attribute('placeholder')}") # Returns value in the 'placeholder' attribute

logo = driver_2.find_element(By.CLASS_NAME, 'python-logo') # element that has classname 'python-logo'
print(f"Logo is : {logo.get_attribute('alt')}") # Returns value in the 'alt' attribute
print(logo.size)

docs_link = driver_2.find_element(By.CSS_SELECTOR, '.download-widget a') # Gets element with that class name and <a> tag
# docs_link = driver_2.find_element(By.CSS_SELECTOR, '.small-widget documentation-widget a')
print(docs_link.text)

submit_bug = driver_2.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a') # Gets element from the XPath
print(submit_bug.text)
driver_2.quit()


