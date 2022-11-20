import re
import requests
from bs4 import BeautifulSoup

"""This file is about Job Notice."""

notices = []
academic ={}

for page in range(1):
    response = requests.get("http://hannam.ac.kr/kor/community/community_01_4.html?pPageNo="+str(page)+"&pRowCount=30&pPageNo=" +str(page+1))
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    word = soup.select('td')  # Excluding Attachments


# Parsing (Excluding Attachments)
    testList = []
    for i in word:
        testList.append(re.sub("\t|\n|\r", "", i.text.strip()).lstrip("번호").lstrip("제목").lstrip("첨부파일").lstrip("작성자").lstrip("작성일").lstrip("조회수"))
        
    for i in range(len(testList)):
        if i % 6 == 0:
            academic = {
                'class' : '취업공지',              # Class
                'number' : testList[i],            # Number
                'title' : testList[i+1],           # Title
                'writer' : testList[i+3],          # Writer
                'dateCreated' : testList[i+4]      # dateCreated
            }
            i += 6
            notices.append(academic)
    
    
# Parsing (Attachment)
    attach = soup.select('.txt-l > a[href]')       # Attachments

    pdfs = {}
    pdfInfoList = []
    
    for i in attach:
        href = i.attrs['href']
        rec = requests.get("http://hannam.ac.kr" + href)
        html = rec.text
        soup = BeautifulSoup(html,"html.parser")
        
        
        noticeTitle = soup.select('.post-title')
        title = noticeTitle[0].text
        pdf = soup.select('.add-file-list > ul > li > a[href]')

        for i in range(len(pdf)):
        
            if pdf[i] != []:
                tmpPdf = "http"+ ((pdf[i].attrs['href']).lstrip("../include/board_down.php?s_filepath="))
                pdfs = {
                'fileName' : tmpPdf[tmpPdf.find('&filename=')+10 : ],
                'fileLink' : tmpPdf[ : tmpPdf.find('&filename=')],
                'title' :  title 
                }
                pdfInfoList.append(pdfs)
                
                
# print result
print(notices)
print(pdfInfoList)   