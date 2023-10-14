import datetime
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.headless = False

profile = webdriver.FirefoxProfile("/home/aditya/.mozilla/firefox/Attendance/")
driver = webdriver.Firefox(options=options, firefox_profile=profile)
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference("useAutomationExtension", False)
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36")


google_sheets_url = 'https://docs.google.com/spreadsheets/d/1sfkGsU7s3h0_L4FjCLlsbvffYOkVlWG6pJIcWvyn9dU/edit#gid=218345889'



# Open the Google Sheets URL
driver.get(google_sheets_url)

# You may need to log in using your university Gmail credentials here

# Wait for the data to load (you can customize the time)
driver.implicitly_wait(12)

# Access the data
#data = driver.find_element_by_css_selector('your-selector').text

# Do something with the data, e.g., print it
#print(data)


def download_sheet():
    file = driver.find_element("id", 'docs-file-menu')
    file.click()

    




driver.quit()
