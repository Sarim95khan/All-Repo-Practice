from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pytesseract import image_to_string

# Replace 'your_image_id' with the actual ID of the CAPTCHA image
image_id = "your_image_id"

# Set Tesseract path (adjust if Tesseract is not in your system path)
# tesseract_path = "path/to/tesseract.exe"  # Replace with your Tesseract installation path
# pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Set up Chrome webdriver (adjust for other browsers)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the webpage containing the CAPTCHA
driver.get("https://www.example.com")  # Replace with the actual URL

# Find the image element by ID
try:
  image_element = driver.find_element(By.ID, image_id)
except:
  print("Image with ID '" + image_id + "' not found!")
  driver.quit()
  exit()

# Capture the entire page screenshot
screenshot = driver.get_screenshot_as_png()

# Get location and size of the image element
location = image_element.location
size = image_element.size

# Crop the screenshot to capture only the image
cropped_screenshot = screenshot[location["x"]:location["x"] + size["width"], location["y"]:location["y"] + size["height"]]

# Convert the cropped screenshot to a PIL image (required by Tesseract)
from io import BytesIO
image = Image.open(BytesIO(cropped_screenshot))

# Extract text from the image using Tesseract OCR
captcha_text = image_to_string(image)

# Print the extracted CAPTCHA text
print("CAPTCHA text:", captcha_text)

# Close the browser
driver.quit()