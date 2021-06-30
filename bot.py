from urllib.request import Request, urlopen as uReq
from bs4 import BeautifulSoup as soup
from twilio.rest import Client 

account_sid = '' #twilio account sid
auth_token = '' #twilio auth token
client = Client(account_sid, auth_token)

url = "https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

btcInfo = page_soup.find("div", {"id":"quote-header-info"})
btcPrice = btcInfo.find("span", {"data-reactid":"33"})
btcChange = btcInfo.find("span", {"data-reactid":"34"})

bodyText = "BTC Price: \t" + str(btcPrice.text) + "\nPrice Change: \t" + str(btcChange.text)
print(bodyText)

message = client.messages.create( 
    from_='',     # twilio phone number, from 
    body=bodyText,      
    to=''         # phone number to send to
)
