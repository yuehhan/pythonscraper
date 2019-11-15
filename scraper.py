import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.ebay.com/itm/Bose-QuietComfort-35-Series-I-Wireless-Headphones-Factory-Renewed/163543329737?epid=572935696&hash=item2613f12bc9%3Am%3AmrVN8YBKOR3ryDWzeb6Clnw&_trkparms=%2526rpp_cid%253D5dc3304b6e4ae02d6d3ffb08&var=462918275683'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="vi-lkhdr-itmTitl").get_text()
    price = soup.find(id="mm-saleDscPrc").get_text()
    #price is a string, must convert
    convertedprice = float(price[4:])

    if (convertedprice < 150.0):
        send_mail()
     
    if (convertedprice > 150.0):
        send_mail()

    

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    #command by email to identify itself to another email server
    server.starttls()
    server.ehlo()

    server.login('cranberrycavalier@gmail.com', 'bpmfxzrhbtpkuoik')

    subject = 'Price went down, check the link!'
    body = 'Check the link https://www.ebay.com/itm/Bose-QuietComfort-35-Series-I-Wireless-Headphones-Factory-Renewed/163543329737?epid=572935696&hash=item2613f12bc9%3Am%3AmrVN8YBKOR3ryDWzeb6Clnw&_trkparms=%2526rpp_cid%253D5dc3304b6e4ae02d6d3ffb08&var=462918275683'

    msg = f"Subject: {subject}\n\n{body}"
     
    server.sendmail(
        'cranberrycavalier@gmail.com',
        'cranberrycavalier@gmail.com',
        msg
    )
    print('Email has been sent!')

    server.quit()


while (True):
    check_price()
    time.sleep(86400)
