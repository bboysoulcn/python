import sqlite3
import smtplib
from email.mime.text import MIMEText
import feedparser

db_connect = sqlite3.connect('/var/tmp/rss.sqlite')
db = db_connect.cursor()
db.execute('CREATE TABLE IF NOT EXISTS magazine (title TEXT,date TEXT)')

def article_is_not_in_db(article_title,article_date):
    db.execute("SELECT * FROM magazine WHERE title=? AND date=?",(article_title,article_date))
    if not db.fetchall():
        return True
    else:
        return False

def add_article_to_db(article_title,article_date):
    db.execute("INSERT INTO magazine VALUES (?,?)",(article_title,article_date))
    db_connect.commit()

def send_mail(article_title,article_url):
    smtp_server = smtplib.SMTP('smtp.gmail.com',587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login('bboysoulcn@gmail.com','google%(!&5917')
    msg = MIMEText(f'\nHi there is a new article:{article_title}.\nYou can read here{article_url}')
    msg['Subject'] = 'new magazine '
    msg['From'] = 'bboysoulcn@gmail.com'
    msg['To'] = 'lifeisnofair@163.com'
    smtp_server.send_message(msg)
    smtp_server.quit()


def read_article_feed():
    feed = feedparser.parse('https://fedoramagazine.org/feed/')
    for article in feed['entries']:
        if article_is_not_in_db(article['title'],article['published']):
            send_mail(article['title'],article['link'])
            add_article_to_db(article['title'],article['published'])

if __name__ == '__main__':
    read_article_feed()
    db_connect.close()