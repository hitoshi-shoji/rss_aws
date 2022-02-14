## rss_aws

(機能1) AWS What's New　RSS情報を取得して、sqlite3 DB(テーブル)へINSERTします。
(機能2) sqlite3 DB(テーブル)のRSS情報全レコードを取得し、AWS What's New情報リスト(Excelファイル)を生成します。

### 環境
Ubuntu 18.04.6 LTS (Bionic Beaver)  
python3.8.0

### (オプション:python仮想環境)
[【venv】Ubuntuでpython仮想環境をつくる](https://qiita.com/komoto2020/items/9837455f8549e06016d8)  
[【Python】venvで仮想環境を作成する【Mac】](https://ymgsapo.com/2020/08/16/how-to-use-venv/)

### 1. ダウンロード
```
$ git clone https://github.com/hitoshi-shoji/rss_aws.git
$ cd rss_aws
```

### 2. モジュールインストール
```
$ pip3 install -r requirements.txt  
or
$ pip install -r requirements.txt
```

### 3. 設定ファイル(settings.py)
#### settingsファイルを開いて設定内容を編集します。
```
## 「rss_url」 は、RSS URLを指定
## 日本語は、"https://aws.amazon.com/jp/about-aws/whats-new/recent/feed/"  
##
rss_url="https://aws.amazon.com/about-aws/whats-new/recent/feed/"  
##
## 「sqlite_dbname」は、データ格納用sqlite3 DB名(ファイル名) 
##
sqlite_dbname="rssaws.db"  
##
## 「output_path」は、Excelファイルの出力先ディレクトリー
##  指定Pathは、事前に作成しておいてください
##  Excelファイル名は、aws-rss-new_YYYYMMDD.HHMMSS.xlsx 固定
##
output_path="/home/ec2-user/"
```

### 4. 実行方法
```
# What's new RSS URLから取得した情報をsqlite3 DB (テーブル:RSS_Table)へINSERT
$ python rss_save_db.py
or
$ python3 rss_save_db.py  

# sqllite3 DB(テーブル：RSS_Table)から全レコードを取得して、Excelファイル作成
$ python rssaws_excel.py
or
$ python3 rssaws_excel.py

```
