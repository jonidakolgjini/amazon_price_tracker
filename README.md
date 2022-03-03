# amazon_price_tracker
Tracks an item price on Amazon, sends email when price is below a set buy price

-	Sends an email whenever the price of an item dips below a set buy price
-	Uses Beautiful Soup package to obtain the item name and price
-	Uses requests package to get the web page html after providing URL of item
-	Uses smtplib package to send the email
-	Could alter program to send a text message using twilio, or automate the program and set it to run at a certain time everyday
