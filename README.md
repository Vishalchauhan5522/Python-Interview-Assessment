# 📊 Web Scraping & Data Analysis with Python

Welcome to the **Web Scraping and Data Analysis** project! This project demonstrates how to scrape commodity price data from a website, convert currency using an API, and export the cleaned data into an Excel file. 🚀

## 📋 Project Overview

This project uses **Selenium** to navigate and scrape a historical data table from [Investing.com](https://uk.investing.com/commodities/us-sugar-no11-historical-data), converts the product prices from USD to INR using an exchange rate API, and exports the processed data to \`Output.xlsx\`. 📈

### 📁 Directory Structure

- **main.py**: Python script that scrapes the data, processes it, and saves it in an Excel file.
- **requirements.txt**: File listing the required Python packages.
- **data.json**: Contains website URL and API key for currency conversion.
- **Output.xlsx**: Final output Excel file with scraped and transformed data.

## ⚙️ Setup Instructions

### Step 1: Clone the repository

```
git clone https://github.com/your-repo-url.git
cd your-repo-name
```

### Step 2: Install Required Dependencies

Make sure you have Python installed (preferably 3.7+). To install the required libraries, run:

```
pip install -r requirements.txt
```

### Step 3: Configure \`data.json\`

In the \`data.json\` file, update the **apiKey** with your own API key from [ExchangeRate API](https://www.exchangerate-api.com/):

```json
{
  "apiKey": "your_api_key_here",
  "website": "https://uk.investing.com/commodities/us-sugar-no11-historical-data",
  "rate_exchange": "https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
}
```
For a time being, a valid api_key is provided in json already, since its a free version api_key. 
Replace with your api_key, if and when API hits failing due to free hits being exhausted.

### Step 4: Run the Script 🚀

Once everything is set up, run the \`main.py\` script:

```bash
python main.py
```

This will:
1. Navigate to the target website.
2. Scrape the product price table.
3. Perform data transformations and currency conversion.
4. Export the results to \`Output.xlsx\`.

## 🧠 Features

- **Web Scraping**: Utilizes Selenium to dynamically interact with the website.
- **Data Processing**: Cleans the data, handles duplicates, and extracts the day of the week.
- **Currency Conversion**: Uses an API to convert USD prices to INR.
- **Excel Export**: Saves the final data in a neatly formatted Excel file.

## 🔧 Technologies Used

- **Python**
- **Selenium** for web scraping 🕸️
- **Pandas** for data manipulation 📊
- **ExchangeRate API** for currency conversion 💱
- **Excel Export** using \`pandas.to_excel\`
