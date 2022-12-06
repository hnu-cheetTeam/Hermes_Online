import re
import requests
from bs4 import BeautifulSoup


"""This file is about Job Notice."""

def academic_notice(num=1):
    """Returns parsed infomation about Job Notice

    Args:
        num (int): number of page for parsing
        
    Returns:
        list : collecion of Dictionary that is Resulf of parsing for Job Notice
    """
    notices = []
    academic ={}
    
    for page in range(num):
        response = requests.get("http://hannam.ac.kr/kor/community/community_01_4.html?pPageNo="+str(page)+"&pRowCount=30&pPageNo=" +str(page+1))
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        word = soup.select('td')  # Excluding Attachments


        # Parsing (Expect Attachments)
        testList = []
        for i in word:
            testList.append(re.sub("\t|\n|\r", "", i.text.strip()).lstrip("번호").lstrip("제목").lstrip("첨부파일").lstrip("작성자").lstrip("작성일").lstrip("조회수"))

        # Parsing (Attachment)
        attach = soup.select('.txt-l > a[href]')       # Attachments 
        
        for i in attach:
            href = i.attrs['href']
            rec = requests.get("http://hannam.ac.kr" + href)
            html = rec.text
            soup = BeautifulSoup(html,"html.parser")
            pdf = soup.select('.add-file-list > ul > li > a[href]')

            fileNameDict = {}
            fileLinkDict = {}
            
            i = 0 
            while (i < len(pdf)):
                tmpPdf = "http"+ ((pdf[i].attrs['href']).lstrip("../include/board_down.php?s_filepath="))
                fileNameDict['file'+ str(i+1)] = tmpPdf[tmpPdf.find('&filename=')+10 : ]
                fileLinkDict['file'+ str(i+1)] = tmpPdf[ : tmpPdf.find('&filename=')]
                i += 1
                
            
            academic = {
                'class' : '취업공지',              # Class
                'number' : testList[0],            # Number
                'title' : testList[1],             # Title
                'writer' : testList[3],            # Writer
                'dateCreated' : testList[4],       # dateCreated
                'postLink' : "http://hannam.ac.kr" + href,
                'fileName' : fileNameDict,
                'fileLink' : fileLinkDict
            }
            
            notices.append(academic)
            testList = testList[6:]
            
            
    return notices



for post in academic_notice(1):
    print(post)
