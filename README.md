# Automated-HAR-File-Generation-and-Analysis
This project demonstrates how to automate the process of capturing and analyzing HTTP Archive (HAR) files using Python and Selenium WebDriver. It involves generating HAR files for a web page and analyzing HTTP response status codes to gain insights into the website's behavior and performance.

# Features:
  Automated Browser Interaction:
    The project uses Selenium to navigate a website and capture performance logs.

  HAR File Generation:
    HTTP Archive (HAR) files are generated to log network activity, such as requests and responses.

  Scroll Automation:
    Automatically scrolls through the web page to capture all network activity.

  Detailed Analysis:
    Analyzes HTTP response codes, categorizes them (2xx, 4xx, 5xx), and saves the results in JSON and TXT formats.

  Organized Output:
    Results are saved in a structured format for easy reference.

README for HAR File Automation Assignment
Project Title:
HAR File Capture and Analysis using Selenium WebDriver

Overview:
This project demonstrates how to automate the process of capturing and analyzing HTTP Archive (HAR) files using Python and Selenium WebDriver. It involves generating HAR files for a web page and analyzing HTTP response status codes to gain insights into the website's behavior and performance.

Features:
Automated Browser Interaction:
The project uses Selenium to navigate a website and capture performance logs.

HAR File Generation:
HTTP Archive (HAR) files are generated to log network activity, such as requests and responses.

Scroll Automation:
Automatically scrolls through the web page to capture all network activity.

Detailed Analysis:
Analyzes HTTP response codes, categorizes them (2xx, 4xx, 5xx), and saves the results in JSON and TXT formats.

Organized Output:
Results are saved in a structured format for easy reference.

# Directory Structure:
PROJECT_PATH/
│
├── chromedriver-win64/                # Contains ChromeDriver executable
│   └── chromedriver.exe
├── HARfiles/                          # Stores generated HAR files
├── output/                            # Contains analysis results (JSON and TXT)
├── testHAR.py                         # Main script for HAR generation and analysis
└── README.md                          # Project documentation

# Prerequisites:
Python: Ensure Python 3.7+ is installed.
Selenium Library: Install Selenium using pip: pip install selenium
Google Chrome: Install the Chrome browser.
ChromeDriver: Download the ChromeDriver version compatible with your Chrome browser. 
Place it in the chromedriver-win64 folder.

# Installation:
Clone or download this repository.
Update the file paths in the script (testHAR.py) to match your system's directory structure:
PROJECT_PATH
CHROME_DRIVER_PATH
HAR_FILES_DIR
OUTPUT_DIR
-------------------------------------------------------------------------------------------------------

# Usage:
Run the Script:
Execute the script using the command:python testHAR.py

# HAR File Generation:
The script navigates to the exactspace.co website, scrolls through the page, and generates a HAR file in the HARfiles directory.

# Analyze HAR File:
The script analyzes the latest HAR file and provides:
  Total number of HTTP requests
  Breakdown of status codes (2xx, 4xx, 5xx)
  Detailed status code counts

# Results:
The analysis results are saved in:

  output/analysis_results.json
  output/analysis_results.txt

# Example Output:
=== Status Code Analysis ===
Total number of requests: 120

Status code category totals:
2XX responses: 100
4XX responses: 10
5XX responses: 5

Detailed status code breakdown:
Status 200: 95
Status 404: 10
Status 500: 5




