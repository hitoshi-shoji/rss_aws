import feedparser
import re
import datetime
import sqlite3
import settings

#dbname = 'rssaws.db'
rss_url = settings.rss_url
dbname = settings.sqlite_dbname

conn = sqlite3.connect(dbname)
cur = conn.cursor()
cur.execute( "CREATE TABLE IF NOT EXISTS RSS_Table ( no INTEGER NOT NULL PRIMARY KEY, id TEXT NOT NULL UNIQUE, category TEXT default 'none' ,published TEXT NOT NULL,title TEXT NOT NULL,summary TEXT,url TEXT NOT NULL)" ) 
conn.commit()

d = feedparser.parse(rss_url)
#d = feedparser.parse('https://aws.amazon.com/about-aws/whats-new/recent/feed/')
reg_obj = re.compile(r"<[^>]*?>")
pattern = ",/a[a-z0-9-]+"

for entry in d.entries:
    id = entry.id
    pubdate_a = entry.published
    pubdate = datetime.datetime.strptime(pubdate_a, '%a, %d %b %Y %H:%M:%S %z').strftime('%Y/%m/%d')
    title = entry.title
    link = entry.link
    category_temp1 = entry.category
    category_temp2 = category_temp1.replace('general:products',',').replace(':','')
    #category_temp2 = category_temp1.replace('marketing:marchitecture',',').replace(':','')
    try:
        category = re.search(pattern, category_temp2).group().replace(',/','')
    except AttributeError:
        category = re.search(pattern, category_temp2)

    summary=reg_obj.sub("",entry.description).replace('&nbsp;','')
    #print(pubdate, category, title, summary, link, sep='~')
    cur.execute("INSERT OR IGNORE INTO RSS_Table (id,category,published,title,summary,url) VALUES (?,?,?,?,?,?)",(id,category,pubdate,title,summary,link))

conn.commit()
cur.close()
conn.close()
