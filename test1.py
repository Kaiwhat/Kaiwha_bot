import requests, time
from bs4 import BeautifulSoup
from datetime import datetime

stock = ['1101', '4904']
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%Y/%m/%d %H:%M:%S")

for i in range(len(stock)):
  stockid = stock[i]
  url = "https://tw.stock.yahoo.com/quote/"+stockid+".TW"
  r= requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  price = soup.find('span', class_=['Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)', 
                                    'Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)', 
                                    'Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)'])
  message = currentTime + "  Stock:" + stockid + "  Price:" + price.getText()
  token = "6485348649:AAExG_jv0GkGqQwMRGGU8CsVMfOy4GAl-JM"
  chat_id = "6258654818"
  url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
  requests.get(url)
  time.sleep(3)

#Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)
#Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)
#Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)
