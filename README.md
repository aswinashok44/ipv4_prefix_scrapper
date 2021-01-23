# IPV4 Prefix Scrapper
Python Script to fetch announced IPv4 prefixes from an ASN via HE's webpage + Automatically filters listed prefixes based on country of Origin
In the sample code we are dealing with AS55836 and filtering only Indian IP prefixes and output it to a text file in RouterOS command syntax

## Requirements
- Python3
	- Selenium
	- Beautifulsoup 4
- Chrome

## Usage
[Download Chrome WebDriver](https://chromedriver.chromium.org/downloads)
Set  **CHROME_WEBDRIVER_PATH** and **OUTPUT_FILE_NAME** variable according to your local environment
To use the script run following commands
```
pip3 install -r requirements.txt
python3 ipv4_prefixes.py
```