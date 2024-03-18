from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from datetime import date
today = date.today()
d1 = today.strftime("%d.%m.%Y")
print("d1 =", d1)

# Initialize the WebDriver
browser = webdriver.Chrome()

url = "https://www.gast.de/portal/center-search/center-search/worldwide"

browser.get(url)
time.sleep(4)

dropdown_xpath = "/html/body/app-root/div/div/app-worldwide-search/div[2]/div[2]/div[2]/form/div[1]/div/select"
dropdown = Select(browser.find_element(By.XPATH, dropdown_xpath))
dropdown.select_by_visible_text("Türkei")

date_input_xpath = '//*[@id="date-from-input"]'
date_input = browser.find_element(By.XPATH, date_input_xpath)
date_input.send_keys(d1)

searchButton_xpath = '/html/body/app-root/div/div/app-worldwide-search/div[2]/div[2]/div[2]/form/button'
searchButton = browser.find_element(By.XPATH,searchButton_xpath)
searchButton.click()
time.sleep(12)

expandDate_xpath = '//*[@id="event-1"]/a'
expandDate = browser.find_element(By.XPATH,expandDate_xpath)
expandDate.click()
time.sleep(1)

stored_elements = {}

for i in range(1, 8):
    place_xpath = f'//*[@id="date-entry-event-1"]/div/div[{i}]/div[1]/a/strong'
    place_element = browser.find_element(By.XPATH, place_xpath)
    place_title = place_element.text

    availability_xpath = f'//*[@id="date-entry-event-1"]/div/div[{i}]/div[3]/form/button'
    availability_element = browser.find_element(By.XPATH, availability_xpath)
    availability_text = availability_element.text

    stored_elements[place_title] = availability_text

print(stored_elements)
for index, (place, status) in enumerate(stored_elements.items(), start=1):
    print(f"{index}- {place} - {status}")

browser.close()
