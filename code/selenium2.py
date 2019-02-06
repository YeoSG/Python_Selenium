from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('../driver/chromedriver')

driver.get('https://goo.gl/VH1A5t')

gu_list_raw = driver.find_element_by_xpath("""//*[@id="SIGUNGU_NM0"]""")
gu_list = gu_list_raw.find_elements_by_tag_name('option')
gu_names = [option.get_attribute("value") for option in gu_list]
gu_names.remove('')
print(gu_names)

element = driver.find_element_by_id("SIGUNGU_NM0")
element.send_keys(gu_names[1])

xpath = """//*[@id="searRgSelect"]"""
element_sel_gu = driver.find_element_by_xpath(xpath).click()

xpath = """//*[@id="glopopd_excel"]"""
element_get_excel = driver.find_element_by_xpath(xpath).click()

driver.close()