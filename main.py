import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import smtplib

load_dotenv()
URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url=URL)
website = response.content

soup = BeautifulSoup(website,"html.parser")
price = float(soup.find(class_="aok-offscreen").getText().split("$")[1])

product_title = soup.find(id="productTitle").getText()
BUY =100
if(BUY < price):
    massage = f"{product_title} is at sale for {price}"

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        connection.login(os.environ["EMAIL_ADDRESS"],os.environ["EMAIL_PASSWPRD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_PASSWORD"],
            massage=f"Subject:Amazon Price Alert!\n\n{massage}".encode("utf-8")
        )