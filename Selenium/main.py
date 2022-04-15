from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

url = 'https://www.adamchoi.co.uk/overs/detailed'

driver.get(url)

#  All Mattches Button
all_matches_btn = driver.find_element( By.XPATH, '//label[@analytics-event="All matches"]' )
all_matches_btn.click()

# Select Country
dropdown_country = Select(driver.find_element( By.ID, 'country' ))
dropdown_country.select_by_visible_text('Germany')

# Matches Table
matches = driver.find_elements(By.TAG_NAME, 'tr')
match_list = []
for match in matches:
    match_list.append(match.text)

df = pd.DataFrame({'Matches': match_list})
df.to_csv('matches.csv', index=False)
time.sleep(10)

driver.quit()