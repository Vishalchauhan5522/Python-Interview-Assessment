import subprocess
import sys

# Install dependencies from requirements.txt
def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
        sys.exit(1)

# Call the install_requirements function
install_requirements()

import time
import pandas as pd
import requests
import json
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load data from JSON file
data_json = []
with open('data.json', 'r') as f:
    data_json = json.load(f)

# Initialize WebDriver and navigate to the website
driver = webdriver.Chrome()
url = data_json['website']
driver.get(url)

# Wait for elements to load dynamically
wait = WebDriverWait(driver, 30)

# Close pop-up if it appears
try:
    pop_up = driver.find_element(By.CLASS_NAME, "signup_isStartScreen__W1o2A")
    close_button = pop_up.find_element(By.CSS_SELECTOR, "form>div>button>svg")
    close_button.click()
    print("Pop-up closed successfully.")
except NoSuchElementException:
    print("No pop-up found, continuing with the script.")

# Interact with the time frame dropdown and select "Weekly"
time_frame_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.mb-4 span.flex-1')))
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.mb-4 span.flex-1')))
time_frame_button.click()

dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.historical-data-v2_menu__uJ2BW")))
weekly_option = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.historical-data-v2_menu__uJ2BW div:nth-child(2)")))
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.historical-data-v2_menu__uJ2BW div:nth-child(2)")))
weekly_option.click()
time.sleep(2)

# Wait for and extract data from the historical data table
table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.mt-6 table')))
tbody = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.mt-6 tbody')))
headers = [header.text.strip() for header in table.find_elements(By.CSS_SELECTOR, "tr th")]
rows = driver.find_elements(By.CSS_SELECTOR, "div.mt-6 tbody tr")

# Extract table data
data = []
for row in rows:
    cols = row.find_elements(By.CSS_SELECTOR, "td")
    row_data = [col.text.strip() for col in cols]
    data.append(row_data)

# Close the WebDriver
driver.quit()

# Create a DataFrame from the extracted data
data = pd.DataFrame(data, columns=['Date', 'Price', 'Open', 'High', 'Low', 'Vol.', 'Change %'])
data['Product Name'] = 'Sugar'

# Convert date and extract the day of the week
data['Product Date'] = pd.to_datetime(data['Date'], format='%b %d, %Y')
data['Day'] = data['Product Date'].dt.day_name()
data['Product Date'] = pd.to_datetime(data['Date'], format='%b %d, %Y').dt.date

# Convert price to float
data['Price'] = data['Price'].astype(float)

# Make an API request to get the exchange rate
api_key = data_json['apiKey']
url_rate_exchange = data_json['rate_exchange'].format(api_key=api_key)
response = requests.get(url_rate_exchange)
response = response.json()

# Extract USD to INR rate and convert the price to INR
usd_to_inr_rate = response['conversion_rates']['INR']
data['Final Price (INR)'] = (data['Price'] * usd_to_inr_rate).round(2)

# Format the price in USD
data['Price'] = data['Price'].apply(lambda x: f"${x:,.2f}")

# Create the final DataFrame with the required columns
final_df = data[['Product Name', 'Price', 'Product Date', 'Day', 'Final Price (INR)']]

# Print the final DataFrame
print(final_df)

# Export the DataFrame to Excel
final_df.to_excel('Output.xlsx', index=False)
print("Data transformation and export completed. The output is written to 'Output.xlsx'.")
