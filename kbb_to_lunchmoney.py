import requests
from selenium import webdriver
from bs4 import BeautifulSoup

mileage = '24000'

#Get this URL by going to kbb.com and following the flow for finding your cars value. Copy the page URL once KBB gives you the price. Replace the mileage in the URL with {} to insert your mileage from the script variable.
car1_url = 'https://www.kbb.com/bmw/5-series/2018/540i-xdrive-sedan-4d/?vehicleid=431625&intent=trade-in-sell&mileage={}&pricetype=private-party&condition=verygood&options=8121036|true'.format(mileage)

browser = webdriver.Firefox()
browser.get(car1_url)
car_value = browser.find_element_by_id("ownersDataIsland").get_attribute("data-privateparty-price")
browser.quit()

headers = {'Authorization': 'Bearer YOUR_LUNCH_MONEY_API_KEY_GOES_HERE'}

payload = {'balance': car_value}
r = requests.put("https://dev.lunchmoney.app/v1/assets/YOUR_LUNCH_MONEY_ASSET_ID_GOES_HERE", data = payload, headers=headers)
