from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pygame
import datetime

# Path to the WebDriver executable
driver_path = 'ADD PATH TO YOUR CHROME DRIVER'

# URL of the website
url = "https://shop.royalchallengers.com/ticket"

# XPath of the element to be queried
# xpath = "/html/body/div[4]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[5]/p"
xpath = "//*[@class='css-q38j1a']"

# Create a new instance of the browser driver
service = Service(executable_path=driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Sound service on board
pygame.mixer.init()
sound = pygame.mixer.Sound('./beep-01a.wav')

try:
    driver.get(url)
    
    while True:
        try:
            div_elements = driver.find_elements("xpath", xpath)
            now = datetime.datetime.now()
            print("\n-------------- {} --------------".format(now))
            for div in div_elements:
                events = div.text.split('\n')

                print("{} {} {}:\t{}".format(events[1], events[2], events[3], events[4]))
                if events[4] != 'SOLD OUT':
                    sound.play()
                    pygame.time.wait(int(sound.get_length() * 1000))
                    print("BOOK: {} {} {}:\t{}".format(events[1], events[2], events[3], events[4]))

        except NoSuchElementException:
            print("Element not found.")
        
        driver.refresh()
        sleep(5)

finally:
    print("QUIT")
    driver.quit()
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))
