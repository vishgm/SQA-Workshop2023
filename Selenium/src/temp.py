from selenium import webdriver

# Set up the Selenium driver for Chrome
driver = webdriver.Chrome()

# Navigate to the bookstore website
driver.get("https://www.example-bookstore.com")

# Find the search bar element and enter a search query
search_bar = driver.find_element_by_name("search")
search_bar.send_keys("The Great Gatsby")

# Find the search button element and click it
search_button = driver.find_element_by_xpath("//button[contains(@class, 'search-btn')]")
search_button.click()

# Verify that the search results contain the expected book
results = driver.find_elements_by_xpath("//div[contains(@class, 'search-result')]")
for result in results:
    if "The Great Gatsby" in result.text:
        print("Book found in search results!")
        break
else:
    print("Book not found in search results.")

# Close the driver
driver.quit()
