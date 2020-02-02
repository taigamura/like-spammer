from selenium import webdriver
import time

for i in range(15):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome("C:/Users/Taiga Kimura/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=chrome_options)
    driver.get('https://note.com/noah_note00/n/n69e62468a2ad')

    # Click button

    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/article/div[4]/div/div[1]/div/div/button').click()

    time.sleep(2)

    driver.close()