from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

CHROME_WEBDRIVER_PATH = 'D:\ipv4_prefix_scrapper\chromedriver.exe'
OUTPUT_FILE_NAME = 'router_os_config.txt'

def get_jio_ipv4_prefix():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(CHROME_WEBDRIVER_PATH,options=chrome_options)
    driver.get('https://bgp.he.net/AS55836#_prefixes')
    sleep(1)
    table = driver.find_element_by_id('table_prefixes4')
    table = table.get_attribute('innerHTML')
    soup = BeautifulSoup(table, 'html.parser')
    driver.close()
    tds = soup.findAll('td',{'class':'nowrap'})
    divs = soup.findAll('div',{'class':'flag alignright floatright'})
    router_os_config_lines = ['/ip firewall address-list\n']
    for i, td, div in zip(range(len(tds)),tds,divs):
        country = div.find('img').get('title')
        ipv4_prefix = td.find('a').text
        print(country,ipv4_prefix)
        if country == 'India':
            config_line = 'add comment="Jio\'s IPv4 Prefixes" list=jio_IPv4_prefixes address=' + str(ipv4_prefix) + '\n'
            router_os_config_lines.append(config_line)
    print(len(router_os_config_lines)-1)
    config_file = open(OUTPUT_FILE_NAME,'w')
    config_file.writelines(router_os_config_lines)
    config_file.close()

if __name__ == '__main__':
    get_jio_ipv4_prefix()
