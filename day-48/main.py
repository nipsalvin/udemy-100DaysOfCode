from selenium import webdriver

url = 'https://alvin254.netlify.app/'
chrome_driver_path = 'C:/Users/Nips/Desktop/Softwares/chromedriver-win64/chromedriver.exe'
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = webdriver.Chrome()

driver.get(url)

# driver.close() #closes tab
driver.quit() #closes browser

