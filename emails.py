import gspread
import pandas as pd
import sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

def getAllMails():
    gc = gspread.service_account(
        filename='/Users/maxhager/Projects2022/Keys/GoogleSheetsKey.json')
    gs = gc.open("HackRetreatSheet").sheet1
    get = gs.get_all_values()
    get = pd.DataFrame(get)
    get = get.iloc[:, 2]
    get = get.tolist()
    get = get[2:]
    return get

def sendMail():
    receiver_emails = getAllMails()
    
    for i in receiver_emails:
        sender_email = "maxhager28@gmail.com"
        receiver_email = i
        password = config.password

        message = MIMEMultipart("alternative")
        message["Subject"] = "HackRetreat"
        message["From"] = sender_email
        message["To"] = receiver_email

        html = """\
        <html>
        <body>
            Hey,
            <br>
            <br>
            Here is Max from HackZurich.
            <br>
            You filled out the form for the <a href="https://yachty66.github.io/HackRetreat/">HackRetreat</a>. We should take some action so I created <a href="https://discord.gg/GpBuKVawea">this</a> Discord channel. 
            <br>
            Please join for seing all the details. It will be great!:)
            <br>
            <br>
            <br>
            Best,
            <br>
            <br>
            Max
            </p>
        </body>
        </html>
        """

        part2 = MIMEText(html, "html")

        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        
if __name__ == "__main__":
    sendMail()