from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Set up options
options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the website
driver.get("https://dining.purdue.edu/menus/")

# Wait for the elements to load
driver.implicitly_wait(5)  # Adjust the wait time as needed

# Find elements by class name
dining_court_options = driver.find_elements(By.CLASS_NAME, "MuiList-root.MuiList-padding.css-1ontqvh")
print(len(dining_court_options))
for option in dining_court_options:
   print(option.text)

# Close the driver
driver.quit()
