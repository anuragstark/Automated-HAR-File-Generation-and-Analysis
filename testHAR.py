from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time
from collections import defaultdict
import os
import glob
from datetime import datetime

#all paths
PROJECT_PATH = r"C:\Users\anuragstark\Desktop\Anurag_Chauhan_SDET"
CHROME_DRIVER_PATH = os.path.join(PROJECT_PATH, "chromedriver-win64", "chromedriver.exe")
HAR_FILES_DIR = os.path.join(PROJECT_PATH, "HARfiles")
OUTPUT_DIR = os.path.join(PROJECT_PATH, "output")

def scroll_page(driver):

    #for scroll up to down
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        #for Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #wait for page load
        time.sleep(2)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def setup_browser_for_har_capture():
    chrome_options = Options()
    
    chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    chrome_options.add_argument('--remote-debugging-port=9222')
    
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def generate_har_file():
    driver = setup_browser_for_har_capture()
    try:
        driver.execute_cdp_cmd('Network.enable', {})
        
        print("Navigating to exactspace.co...")
        driver.get("https://exactspace.co/")
        
        # Waiit for page load
        time.sleep(5)
        
        #page scrolling
        print("Scrolling through the page...")
        scroll_page(driver)
        
        # Waiting for req.
        time.sleep(5)
        
        logs = driver.get_log('performance')
        
        #convert logs into HAR format
        har_entries = []
        for log in logs:
            if 'message' in log:
                message = json.loads(log['message'])
                if 'message' in message and message['message'].get('method') == 'Network.responseReceived':
                    params = message['message'].get('params', {})
                    response = params.get('response', {})
                    
                    entry = {
                        'response': {
                            'status': response.get('status', 0),
                            'url': response.get('url', ''),
                            'headers': response.get('headers', {})
                        }
                    }
                    har_entries.append(entry)
        
        #HAR file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        har_file_path = os.path.join(HAR_FILES_DIR, f'capture_{timestamp}.har')
        
        har_data = {
            'log': {
                'version': '1.2',
                'creator': {'name': 'Custom HAR Generator', 'version': '1.0'},
                'entries': har_entries
            }
        }
        
        #For Saving HAR file
        with open(har_file_path, 'w', encoding='utf-8') as f:
            json.dump(har_data, f, indent=2)
            
        print(f"HAR file saved: {har_file_path}")
        
    finally:
        driver.quit()


def get_latest_har_file():
    list_of_files = glob.glob(os.path.join(HAR_FILES_DIR, '*.har'))
    if not list_of_files:
        raise FileNotFoundError("No HAR files found in the specified directory")
    return max(list_of_files, key=os.path.getctime)

def analyze_har_file():
    try:
        #select always latest file
        har_file_path = get_latest_har_file()
        print(f"\nAnalyzing HAR file: {os.path.basename(har_file_path)}")
        
        status_counts = defaultdict(int)
        
        with open(har_file_path, 'r', encoding='utf-8') as f:
            har_data = json.load(f)
        
        entries = har_data['log']['entries']
        
        for entry in entries:
            status_code = entry['response']['status']
            status_counts[status_code] += 1
        
        total_2xx = sum(status_counts[code] for code in status_counts if 200 <= code < 300)
        total_4xx = sum(status_counts[code] for code in status_counts if 400 <= code < 500)
        total_5xx = sum(status_counts[code] for code in status_counts if 500 <= code < 600)
        total_requests = sum(status_counts.values())
        
        #for results
        results = {
            "total_requests": total_requests,
            "status_code_categories": {
                "2xx_responses": total_2xx,
                "4xx_responses": total_4xx,
                "5xx_responses": total_5xx
            },
            "detailed_status_codes": dict(status_counts)
        }
        
        #for sav in JSON format
        json_output_path = os.path.join(OUTPUT_DIR, "analysis_results.json")
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        
        #for save in txt frmat
        txt_output_path = os.path.join(OUTPUT_DIR, "analysis_results.txt")
        with open(txt_output_path, 'w', encoding='utf-8') as f:
            f.write("=== Status Code Analysis ===\n")
            f.write(f"Total number of requests: {total_requests}\n\n")
            
            f.write("Status code category totals:\n")
            f.write(f"2XX responses: {total_2xx}\n")
            f.write(f"4XX responses: {total_4xx}\n")
            f.write(f"5XX responses: {total_5xx}\n\n")
            
            f.write("Detailed status code breakdown:\n")
            for status, count in sorted(status_counts.items()):
                f.write(f"Status {status}: {count}\n")
        
        #Print in console
        print("\n=== Status Code Analysis ===")
        print(f"Total number of requests: {total_requests}")
        
        print("\nStatus code category totals:")
        print(f"2XX responses: {total_2xx}")
        print(f"4XX responses: {total_4xx}")
        print(f"5XX responses: {total_5xx}")
        
        print("\nDetailed status code breakdown:")
        for status, count in sorted(status_counts.items()):
            print(f"Status {status}: {count}")
            
        print(f"\nResults saved to:")
        print(f"- {json_output_path}")
        print(f"- {txt_output_path}")
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred while analyzing the HAR file: {e}")

def main():
    #this will create the dir for txt nd JSON format file
    os.makedirs(HAR_FILES_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("Starting HAR file generation...")
    generate_har_file()
    
    print("Starting HAR file analysis...")
    analyze_har_file()

if __name__ == "__main__":
    main()