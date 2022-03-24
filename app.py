from pyvirtualdisplay import Display
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from flask import Flask
from webdriver_manager.chrome import ChromeDriverManager 

app = Flask(__name__)


@app.route('/')
def home():
    return "seja bem vindo"

@app.route('/place/<place>')
def search_place(place):
    display = Display()
    display.start()
    
    place = place
    xpath_address = '//*[@id="searchboxinput"]'
    button_search_latlong ='//*[@id="searchbox-searchbutton"]'
    lat_xpath = '//*[@id="lat"]'
    long_xpath = '//*[@id="lat"]'
    browser = webdriver.Chrome(ChromeDriverManager().install())
    try:
        browser.get('https://www.google.com.br/maps/')
        
        while len(browser.find_elements(by=By.XPATH , value= xpath_address)) < 1:
                continue
        
        browser.find_element(by=By.XPATH , value= xpath_address).send_keys(place)
        browser.find_element(by=By.XPATH , value= button_search_latlong).click()
        # lat_result =  browser.find_element(by=By.XPATH , value= lat_xpath)
        # long_result =  browser.find_element(by=By.XPATH , value= long_xpath)
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
