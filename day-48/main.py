from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
url2 = 'https://www.python.org/'
# chrome_driver_path = 'C:/Users/Nips/Desktop/Softwares/chromedriver-win64/chromedriver.exe'
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

title = driver.title
price= driver.find_element(By.CLASS_NAME, 'a-offscreen')
print(title)
print(f"Price: {price.get_attribute('innerHTML')}")

## TODO: Complete the code below
# driver = webdriver.Chrome()
# driver.get(url2)

# search_bar = driver.find_element

# driver.close() #closes tab
driver.quit() #closes browser


