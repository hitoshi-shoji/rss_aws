import sqlite3
import openpyxl
import datetime
import os
import settings
from openpyxl.styles.fonts import Font
from openpyxl.styles.borders import Border, Side
from openpyxl.styles import Alignment
from openpyxl.styles import PatternFill

workbook = openpyxl.Workbook()
sheet = workbook.active

border = Border(top=Side(style='thin', color='000000'), 
    bottom=Side(style='thin', color='000000'), 
    left=Side(style='thin', color='000000'),
    right=Side(style='thin', color='000000')
)

fill = PatternFill(patternType='solid',fgColor='00FFFF')

sheet['A2'].value = 'No.'
sheet['B2'].value = '投稿日'
sheet['C2'].value = 'サービス'
sheet['D2'].value = 'アップデートタイトル'
sheet['E2'].value = '概要'
sheet['F2'].value = '調査対象'
sheet.auto_filter.ref = "A2:F2"

for abc in ['A','B','C','D','E','F']:
    sheet[abc + '2'].font = Font(name='Meiryo',size='10',bold=True)
    sheet[abc + '2'].border = border 
    sheet[abc + '2'].alignment = Alignment(horizontal='center', vertical='center') 
    sheet[abc + '2'].fill = fill 

db = sqlite3.connect('rssaws.db')
cur = db.cursor()
cur.execute('SELECT no,published,category,title,url,summary FROM RSS_Table order by published desc')
for i, row in enumerate (cur):
    sheet['A' + str(i+3)].value =  (i+1)
    sheet['B' + str(i+3)].value = row[1] 
    sheet['C' + str(i+3)].value = row[2] 
    sheet['D' + str(i+3)].value = row[3] 
    sheet['D' + str(i+3)].hyperlink = row[4]
    sheet['D' + str(i+3)].style = "Hyperlink"
    sheet['E' + str(i+3)].value = row[5] 

cur.close()

for rows0 in sheet['A3':'A1000']:
    for cell0 in rows0:
        cell0.font = Font(name='Meiryo',size='9')
        cell0.border = border
        cell0.alignment = Alignment(horizontal='center', vertical='center')

for rows1 in sheet['B3':'C1000']:
    for cell1 in rows1:
        cell1.font = Font(name='Meiryo',size='9')
        cell1.border = border
        cell1.alignment = Alignment(horizontal='left', vertical='center', wrapText=True)

for rows2 in sheet['D3':'D1000']:
    for cell2 in rows2:
        cell2.font = Font(name='Meiryo',size='9',color='0000FF')
        cell2.border = border
        cell2.alignment = Alignment(horizontal='left', vertical='top', wrapText=True)

for rows3 in sheet['E3':'E1000']:
    for cell3 in rows3:
        cell3.font = Font(name='Meiryo',size='9')
        cell3.border = border
        cell3.alignment = Alignment(horizontal='left', vertical='top', wrapText=True)

for rows4 in sheet['F3':'F1000']:
    for cell4 in rows4:
        cell4.font = Font(name='Meiryo',size='9')
        cell4.border = border
        cell4.alignment = Alignment(horizontal='center', vertical='center')

sheet.column_dimensions['A'].width = 4
sheet.column_dimensions['B'].width = 12
sheet.column_dimensions['C'].width = 20
sheet.column_dimensions['D'].width = 55 
sheet.column_dimensions['E'].width = 82 
sheet.column_dimensions['F'].width = 12 
sheet.freeze_panes = 'A3'

now = datetime.datetime.now()
filename = settings.output_path + 'aws-rss-new_' + now.strftime('%Y%m%d.%H%M%S') + '.xlsx'
workbook.save(filename)
