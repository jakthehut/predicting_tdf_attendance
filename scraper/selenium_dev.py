from selenium import webdriver
from selenium.webdriver.common.by import By
import re


URL_rider = "https://www.procyclingstats.com/rider/primoz-roglic/2021"
driver = webdriver.Chrome()  # You should have the Chrome WebDriver installed and in your PATH
driver.get(URL_rider)


def find_birthyear(driver):
    """Return birth year of the rider"""

    rider_info_age = driver.find_element(By.CLASS_NAME, "rdr-info-cont")
    date_of_birth_pattern = r'Date of birth:</b> (\d{1,2})<sup>th</sup> (\w+) (\d{4})'

    match = re.search(date_of_birth_pattern, rider_info_age.get_attribute("innerHTML"))
    if match:
        year = match.group(3)
        if year != "-":
            return year
    return None

birthyear = find_birthyear(driver)

profile={}
if birthyear is not None:
    age_in_2021 = 2021 - int(birthyear)
    profile = {"age that season": age_in_2021}

print(profile)
# Close the webdriver when done
driver.quit()

