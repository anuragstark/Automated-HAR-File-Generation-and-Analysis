# Automated HAR File Generation and Analysis

## Project Overview
This project is a Python-based tool designed to automate HAR (HTTP Archive) file generation and analyze HTTP responses. Using Selenium, it captures network activity from a web page, generates HAR files, and provides detailed analysis of HTTP status codes. The tool saves the results in JSON and TXT formats for further reference.

---

## Features
- Automated browser navigation and dynamic page scrolling to capture all network activity.
- HAR file generation for detailed tracking of HTTP requests and responses.
- Categorized analysis of HTTP status codes (2XX, 4XX, 5XX).
- Output results saved in both JSON and TXT formats for easy accessibility.

---

## Technologies Used
- **Programming Language:** Python
- **Libraries/Frameworks:** Selenium, JSON
- **Tools:** ChromeDriver

---

## Project Structure
```
Anurag_Chauhan_SDET/
|-- chromedriver-win64/          # Directory containing ChromeDriver
|   |-- chromedriver.exe
|
|-- HARfiles/                    # Directory for storing generated HAR files
|
|-- output/                      # Directory for saving analysis results
|   |-- analysis_results.json
|   |-- analysis_results.txt
|
|-- testHAR.py                   # Main script file
```

---

## Prerequisites
1. Python 3.x installed.
2. Selenium library installed. Run the command:
   ```bash
   pip install selenium
   ```
3. Chrome browser installed.
4. Compatible ChromeDriver version matching your browser. Download it from [ChromeDriver](https://chromedriver.chromium.org/downloads).

---

## Setup Instructions
1. Clone the repository or download the project files.
2. Place the ChromeDriver executable in the `chromedriver-win64` folder.
3. Update the following paths in the `testHAR.py` file:
   - `PROJECT_PATH` (Base directory for your project).
   - `CHROME_DRIVER_PATH` (Path to your ChromeDriver executable).
   - `HAR_FILES_DIR` (Directory to save HAR files).
   - `OUTPUT_DIR` (Directory to save analysis results).
4. Run the script:
   ```bash
   python testHAR.py
   ```

---

## Usage
1. **HAR File Generation:**
   - Automatically captures network activity from the specified website (default: `https://exactspace.co`).
   - Saves the generated HAR file in the `HARfiles` directory.

2. **HAR File Analysis:**
   - Analyzes the latest HAR file.
   - Categorizes HTTP responses (2XX, 4XX, 5XX).
   - Saves results in JSON and TXT formats in the `output` directory.

---

## Example Output
### JSON Output
```json
{
  "total_requests": 150,
  "status_code_categories": {
    "2xx_responses": 120,
    "4xx_responses": 20,
    "5xx_responses": 10
  },
  "detailed_status_codes": {
    "200": 110,
    "404": 15,
    "500": 8
  }
}
```

### TXT Output
```
=== Status Code Analysis ===
Total number of requests: 150

Status code category totals:
2XX responses: 120
4XX responses: 20
5XX responses: 10

Detailed status code breakdown:
Status 200: 110
Status 404: 15
Status 500: 8


