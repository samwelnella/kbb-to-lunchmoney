from typing import cast
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--verbose')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument("--log-level=0")

# browser = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
browser = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options,service_args=['--verbose'], service_log_path='/tmp/chrome.log')
browser.implicitly_wait(2)
browser.implicitly_wait(2)

import requests
import os
import dateutil
from lxml import etree

from selenium import webdriver
from bs4 import BeautifulSoup

kbb_url = os.getenv('KBB_URL')

# estimate additional mileage
# if mileage_start_date := os.environ.get('MILEAGE_START_DATE'):
#   average_yearly_mileage = os.getenv('MILEAGE_PER_YEAR', 12_000)
#   average_yearly_mileage = int(average_yearly_mileage)

#   dateutil.relativedelta.relativedelta(mileage_start_date, datetime.now())

#   mileage_start_date = mileage_start_da\
#Get this URL by going to kbb.com and following the flow for finding your cars value. Copy the page URL once KBB gives you the price. Replace the mileage in the URL with {} to insert your mileage from the script variable.
car1_url = 'https://www.kbb.com/bmw/5-series/2018/540i-xdrive-sedan-4d/?vehicleid=431625&intent=trade-in-sell&mileage=100&pricetype=private-party&condition=verygood&options=8121036|true'
browser.get(car_url)
print(browser.page_source)
car_value_svg_url = browser.find_element_by_tag_name("object").get_attribute("data")

browser.get(car_value_svg_url)
browser.quit()

svg_content = requests.get(car_value_svg_url).content
svg_tree = etree.fromstring(svg_content)
car_value = svg_tree.xpath("//*[@id='RangeBox']/svg:text[4]/text()", namespaces={"svg":"http://www.w3.org/2000/svg"})[0]

print(f'Car value: {car_value}')

# headers = {'Authorization': os.getenv('LUNCHMONEY_KEY')}

# payload = {'balance': car_value}
# r = requests.put(f"https://dev.lunchmoney.app/v1/assets/{os.getenv("LUNCHMONEY_ASSET_ID)}", data=payload, headers=headers)
