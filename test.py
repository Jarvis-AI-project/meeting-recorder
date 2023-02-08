import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--profile-directory=Default')
options.add_argument('--user-data-dir=C:\\Users\\AARUSH\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
driver = uc.Chrome(options=options)
driver.user_data_dir=r'C:\Users\AARUSH\AppData\Local\Google\Chrome\User Data\Default'
driver.get('https://www.youtube.com/')
time.sleep(50)
driver.quit()

