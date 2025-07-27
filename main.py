import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import smtplib

load_dotenv()
URL = "https://www.amazon.in/CMF-NOTHING-Buds-Dirac-Tuned-Bluetooth/dp/B0FFN49G12/"
header = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0",
    "Accept-Language" : "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "upgrade-insecure-requests" : "1",
    "sec-fetch-dest": "document",
    "sec-fetch-mode" : "navigate",
    "sec-fetch-site" : "cross-site",
    "sec-fetch-user" : "?1",
    "dnt" : "1",
    "sec-gpc" : "1",
}

response = requests.get(url=URL, headers=header)
website = response.content

soup = BeautifulSoup(website,"html.parser")
price = float(soup.find(class_="a-price-whole").getText().replace(",","").replace(".",""))
print(price)

product_title = soup.find(id="productTitle").getText().strip()
print(product_title)
BUY =2200
if(price <= BUY):
    massage = f"{product_title} is at sale for {price}"

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        connection.login(os.environ["EMAIL_ADDRESS"],os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["TO_EMAIL"],
            msg=f"Subject:Amazon Price Alert!\n\n{massage}".encode("utf-8")
        )