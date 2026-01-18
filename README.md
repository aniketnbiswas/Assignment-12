# Assignment-12
# Amazon Product Scraper

## Project Overview
This Python script uses Selenium to automate the Google Chrome browser. It navigates to Amazon.in, searches for "iphones," and extracts a text list of all product titles found on the first page of results.

## Why We Changed the Approach (Video vs. Current Code)

If you compare this code to older tutorials (like the one originally followed), you will notice significant changes. These were necessary to fix errors caused by software updates.

### 1. Syntax Update: Selenium 3 vs. Selenium 4
* **The Tutorial Approach:** Used commands like `driver.find_element_by_xpath(...)`.
* **The Problem:** The `_by_xpath` commands were **deprecated and removed** in Selenium 4 (the current version). Using them now causes an `AttributeError`.
* **Our Solution:** We migrated to the modern syntax using `By`:
    ```python
    # Old
    driver.find_element_by_xpath("...")
    
    # New
    from selenium.webdriver.common.by import By
    driver.find_element(By.XPATH, "...")
    ```

### 2. Strategy Update: Handling "Code Rot" on Amazon
* **The Tutorial Approach:** Attempted to find products by matching exact CSS classes like `a-size-medium a-color-base a-text-normal`.
* **The Problem:** Amazon frequently updates their website's styling code. The specific class combination from the video no longer exists on the live site, resulting in **0 items found**.
* **Our Solution:** We switched to a **Structural XPath**.
    * Instead of looking for a font style (which changes), we now target the "Search Result Component" container (`data-component-type='s-search-result'`).
    * This is a "robust" locator strategy that continues to work even if Amazon changes their font sizes or colors.

### 3. Stability Update: Smart Waits
* **The Tutorial Approach:** Used `time.sleep()` or no waits at all.
* **The Problem:** The script would sometimes crash if the internet connection was slightly slow, trying to find elements before they loaded.
* **Our Solution:** We implemented `WebDriverWait`. This intelligently pauses the script *only* until the specific element (like the search box) is actually ready to be clicked.

## Installation & Usage

1.  **Install Requirements:**
    ```bash
    pip install selenium webdriver-manager
    ```

2.  **Run the Script:**
    ```bash
    python sel_1.py
    ```
