from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = 'https://en.wikipedia.org/wiki/Main_Page'

driver = webdriver.Firefox()
driver.get(url)

article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')

# article_count.click()

link_text = driver.find_element(By.LINK_TEXT, 'Log in')
# link_text.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys('Dry Associates')
search.send_keys(Keys.ENTER)


# driver.quit()



