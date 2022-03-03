from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os

EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["PASSWORD"]
TARGET_EMAIL = os.environ["TARGET_EMAIL"]

URL="https://www.amazon.co.uk/Oral-B-CrossAction-Toothbrush-Connected-Whitening/dp/B01DY36JF4?ref_=Oct_DLandingS_D_0f40ad14_61&smid=A3P5ROKL5A1OLE"

headers = {
    "Accept-Language": "en-GB,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"
}

response = requests.get(URL, headers=headers)
response.raise_for_status()
web_page = response.text
soup = BeautifulSoup(web_page, "lxml")

item_name = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break").get_text().strip()
price = soup.find(name="span", class_="a-offscreen").get_text()
price_floating_point = float(price.split("£")[1])

BUY_PRICE = 200

if price_floating_point < BUY_PRICE:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=TARGET_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{item_name} is now {price}\n{URL}".encode("utf-8")
        )
        connection.close()
