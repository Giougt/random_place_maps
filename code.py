from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import pyautogui
import webbrowser
import time
import random 

chromedriver_path = " path"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

def random_coordinates():
    latitude = round(random.uniform(-90, 90), 7)
    longitude = round(random.uniform(-180, 180), 7)
    altitude = random.randint(0, 100000)
    return f"{latitude},{longitude},{altitude}"


coordonnates = "https://www.google.fr/maps/@" + random_coordinates() + "m/"

#open maps 
webbrowser.open(coordonnates)

time.sleep(4)
screenshot = pyautogui.screenshot()
screenshot.save("maps_target.png")
