from click import option
from pyvirtualdisplay import Display
import os
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask
from webdriver_manager.chrome import ChromeDriverManager 



app = Flask(__name__)


@app.route("/")
def home():
    return search_place(addres= "rua aiguara")

@app.route("/place/<addres>")
def search_place(addres):
    place = addres
   # display = Display(visible=False, size=(800, 600))
    #display.start()
    # browser = webdriver.Chrome(executable_path=chrome_options.binary_location, chrome_options= chrome_options)
    

    GOOGLE_CHROME_BIN = os.environ.get('/app/.apt/usr/bin/google-chrome')
    #GOOGLE_CHROME_BIN = os.environ.get('chromedriver')
    options = webdriver.ChromeOptions()
    options.binary_location = GOOGLE_CHROME_BIN
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument('--headless')
    options.add_argument('--remote-debugging-port=9222')
    
    browser = webdriver.Chrome(executable_path=(r'./chromedriver.exe'),options= options )

    xpath_address = '//*[@id="searchboxinput"]'
    button_search_latlong ='//*[@id="searchbox-searchbutton"]'
    
    #browser = webdriver.Chrome(ChromeDriverManager().install())
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
