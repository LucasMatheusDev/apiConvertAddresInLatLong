# from pyvirtualdisplay import Display
import os
from numpy import place
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask
from webdriver_manager.chrome import ChromeDriverManager 



app = Flask(__name__)


@app.route("/")
def home():
    return search_place(place= "rua aiguara 156")

@app.route("/place/<place>")
def search_place(place):
    # display = Display(visible=False, size=(800, 600))
    # display.start()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options= chrome_options)


    place = place
    xpath_address = '//*[@id="searchboxinput"]'
    button_search_latlong ='//*[@id="searchbox-searchbutton"]'
    
    # browser = webdriver.Chrome("chromedriver")
    try:
        browser.get('https://www.google.com.br/maps/')
        
        while len(browser.find_elements(by=By.XPATH , value= xpath_address)) < 1:
                continue
        
        browser.find_element(by=By.XPATH , value= xpath_address).send_keys(place)

        browser.find_element(by=By.XPATH , value= button_search_latlong).click()

        while not browser.current_url.__contains__("@"):
                continue

        url_current = browser.current_url
        result =  url_current.split("@")
        simple = result[1].split(",17z")
        info = simple[0]
        lat_long = {"lat" : info.split(",")[0] , "long" : info.split(',')[1]}
        print(f"lat long {lat_long}")        
        # lat_long = {"lat" : lat_result.text , "long" : long_result.text}
        return lat_long



    finally:
        browser.quit()
        # display.stop() 


if __name__ == "__main__":
    app.run(debug=True)
