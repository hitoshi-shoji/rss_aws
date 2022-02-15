#### settings.py
### "rss_new_url" は、What's new AWS RSS URLを指定
rss_new_url="https://aws.amazon.com/about-aws/whats-new/recent/feed/"
### AWS blog RSS 取得の場合は、true
rss_blog="true"
### "rss_blog_url" は、AWS blog RSS URLを指定
rss_blog_url="https://aws.amazon.com/blogs/aws/feed/"
### 「sqlite_dbname」は、データ格納用sqlite3 DB名(ファイル名)を指定
sqlite_dbname="rssaws.db"
## 「output_path」は、Excelファイルの出力先ディレクトリー
##  指定Pathは、事前に作成しておいてください
##  Excelファイル名は、aws-rss-new_YYYYMMDD.HHMMSS.xlsx 固定
output_path="/home/ubuntu/"
