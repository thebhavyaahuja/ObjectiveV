from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/mess', methods=['POST'])
def mess():
    data = request.get_json()
    usern = data['username']
    passw = data['password']
    url = 'mess.iiit.ac.in'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://"+url)
    time.sleep(5)

    if ('login' in driver.current_url) :
        By = webdriver.common.by.By
        username = driver.find_element(By.ID, 'username')
        username.send_keys(usern)
        password = driver.find_element(By.ID, 'password')
        password.send_keys(passw)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    table = soup.find('table')
    rows = table.find_all('tr')
    breakfast = str(rows[5]).split('<td>')[2].split('</td>')[0]
    lunch = str(rows[6]).split('<td>')[2].split('</td>')[0]
    dinner = str(rows[7]).split('<td>')[2].split('</td>')[0]
    meal=""

    current_time = time.localtime()
    if current_time.tm_hour < 10 :
        meal='Breakfast'
        print(breakfast)
    elif current_time.tm_hour < 15 :
        meal='Lunch'
        print(lunch)
    else :
        meal='Dinner'
        print(dinner)

    # get meal data from iiit-mess.in


    driver.quit()

if __name__ == '__main__':
    app.run()