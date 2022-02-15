import feedparser
import re
import datetime
import sqlite3
import settings
import sys

rss_new_url = settings.rss_new_url
rss_blog = settings.rss_blog
rss_blog_url = settings.rss_blog_url
dbname = settings.sqlite_dbname

if not dbname:
    print ("sqlite_dbname is not settings.py")
    sys.exit(1)
if not rss_new_url:
    print ("rss_new_url is not settings.py")
    sys.exit(1)

def main():
    rss_new_save_db()
    if rss_blog == "true":
        rss_blog_save_db()

def rss_new_save_db():   
    
    conn1 = sqlite3.connect(dbname)
    cur1 = conn1.cursor()
    cur1.execute( "CREATE TABLE IF NOT EXISTS rss_new_table ( no INTEGER NOT NULL PRIMARY KEY, id TEXT NOT NULL UNIQUE, category TEXT default 'none' ,published TEXT NOT NULL,title TEXT NOT NULL,summary TEXT,url TEXT NOT NULL)" ) 
    conn1.commit()

    dnew = feedparser.parse(rss_new_url)
    reg_obj = re.compile(r"<[^>]*?>")
    pattern = ",/a[a-z0-9-]+"

    for entry1 in dnew.entries:
        id1 = entry1.id
        pubdate_new = entry1.published
        pubdate1 = datetime.datetime.strptime(pubdate_new, '%a, %d %b %Y %H:%M:%S %z').strftime('%Y/%m/%d')
        title1 = entry1.title
        link1 = entry1.link
        category1_temp1 = entry1.category
        category1_temp2 = category1_temp1.replace('general:products',',').replace(':','')
        ###category_temp2 = category_temp1.replace('marketing:marchitecture',',').replace(':','')
        try:
            category1 = re.search(pattern, category1_temp2).group().replace(',/','')
        except AttributeError:
            category1 = re.search(pattern, category1_temp2)

        summary1=reg_obj.sub("",entry1.description).replace('&nbsp;','')
        cur1.execute("INSERT OR IGNORE INTO rss_new_table (id,category,published,title,summary,url) VALUES (?,?,?,?,?,?)",(id1,category1,pubdate1,title1,summary1,link1))

    conn1.commit()
    cur1.close()
    conn1.close()

def rss_blog_save_db():    
    
    conn2 = sqlite3.connect(dbname)
    cur2 = conn2.cursor()
    cur2.execute( "CREATE TABLE IF NOT EXISTS rss_blog_table ( no INTEGER NOT NULL PRIMARY KEY, id TEXT NOT NULL UNIQUE, category TEXT default 'none' ,published TEXT NOT NULL,title TEXT NOT NULL,summary TEXT,url TEXT NOT NULL)" ) 
    conn2.commit()

    dblog = feedparser.parse(rss_blog_url)

    for entry2 in dblog.entries:
        id2 = entry2.id
        pubdate_blog = entry2.published
        pubdate2 = datetime.datetime.strptime(pubdate_blog, '%a, %d %b %Y %H:%M:%S %z').strftime('%Y/%m/%d')
        category2 = entry2.category
        title2 = entry2.title
        link2 = entry2.link
        summary2=entry2.description
        cur2.execute("INSERT OR IGNORE INTO rss_blog_table (id,category,published,title,summary,url) VALUES (?,?,?,?,?,?)",(id2,category2,pubdate2,title2,summary2,link2))

    conn2.commit()
    cur2.close()
    conn2.close()

if __name__ == "__main__":
    main()