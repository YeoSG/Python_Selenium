from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('../driver/chromedriver')

# driver.get("http://www.daum.net")

# driver.save_screenshot('../images/first_scr1.jpg')

# elem_login = driver.find_element_by_id("id")
# elem_login.clear()
# elem_login.send_keys("********")

# elem_login = driver.find_element_by_id("pw")
# elem_login.clear()
# elem_login.send_keys("********")

driver.get("https://inslab.co.kr")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

f= open('../code/html_content.html','w', encoding='UTF-8', newline='')
f.write(str(soup))
f.close

driver.close()