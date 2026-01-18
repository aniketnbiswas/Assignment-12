from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Setup Driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.amazon.in')

try:
    # 2. Search for iPhones
    # Wait up to 10 seconds for the search box to appear
    wait = WebDriverWait(driver, 10)
    
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.send_keys('iphones')
    
    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()

    # 3. Wait specifically for the "Search Results" to be visible
    # This targets the actual blocks of products, not just any text
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']")))

    # 4. Extract Titles using a robust Locator
    # We look inside the "search result" block -> find the Header (h2) -> find the Text (span)
    title_elements = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']//h2//span")

    # 5. Create the clean list
    phone_list = []
    
    for title in title_elements:
        name = title.text
        # Only add if the name is not empty
        if name: 
            phone_list.append(name)

    # 6. Print the Final List
    print(f"Successfully scraped {len(phone_list)} phones:")
    print("-" * 30)
    for phone in phone_list:
        print(phone)

except Exception as e:
    print("An error occurred:", e)

# Keep browser open to verify
input("Press Enter to close...")
driver.quit()