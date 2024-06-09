from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pytesseract import image_to_string
import requests
from PIL import Image
from PIL import Image
from io import BytesIO

def get_captcha_text(location, size):
    im = Image.open('screenshot.png') # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']


    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('screenshot.png')
    captcha_text = image_to_string(Image.open('screenshot.png'))
    return captcha_text 

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome( )
driver.set_window_size(1120, 1000)

url_path = "https://blsitalypakistan.com/account/login"
google = "https://google.com"

driver.get(url_path)

captcha_image = driver.find_element(By.ID, 'Imageid')
catpcha_src= captcha_image.get_attribute('src')
print("Captcha image src = ",catpcha_src )


location = captcha_image.location
print('Location: ',location)
size = captcha_image.size
captcha_text = get_captcha_text(location, size)
print("catpcha text: ",captcha_text)




time.sleep(40)

driver.quit()