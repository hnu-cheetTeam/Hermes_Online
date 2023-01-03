import re
import requests
import json
from bs4 import BeautifulSoup


"""This file is about Academic Notice."""

def academic_notice(num=1):
    """Returns parsed infomation about Academic Notice

    Args:
        num (int): number of page for parsing
        
    Returns:
        list : collecion of Dictionary that is Resulf of parsing for Accademic Notice
    """
    notices = {}
    academic ={}
    
    for page in range(num):
        response = requests.get("http://hannam.ac.kr/kor/guide/guide_02.html?pPageNo="+str(page)+"&pRowCount=30&pPageNo=" +str(page+1))
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        word = soup.select('td')  # Excluding Attachments


        # Parsing (Expect Attachments)
        testList = []
        for i in word:
            testList.append(re.sub("\t|\n|\r", "", i.text.strip()).replace("번호", "").replace("제목", "").replace("작성자", "").replace("작성일", " "))

        # Parsing (Attachment)
        attach = soup.select('.txt-l > a[href]')       # Attachments 
        idx = 0
        for i in attach:
            href = i.attrs['href']
            rec = requests.get("http://hannam.ac.kr" + href)
            html = rec.text
            soup = BeautifulSoup(html,"html.parser")
            pdf = soup.select('.add-file-list > ul > li > a[href]')

            fileNameDict = {}
            fileLinkDict = {}
            recentReadUser = {}
            
            i = 0 
            while (i < len(pdf)):
                tmpPdf = "http"+ ((pdf[i].attrs['href']).lstrip("../include/board_down.php?s_filepath="))
                fileNameDict['file'+ str(i+1)] = tmpPdf[tmpPdf.find('&filename=')+10 : ]
                fileLinkDict['file'+ str(i+1)] = tmpPdf[ : tmpPdf.find('&filename=')]
                i += 1
                
            
            academic = {
                'class' : '학사공지',              # Class
                'number' : testList[0],            # Number
                'title' : testList[1],             # Title
                'writer' : testList[3],            # Writer
                'dateCreated' : testList[4],       # dateCreated
                'postLink' : "http://hannam.ac.kr" + href,
                'fileName' : fileNameDict,
                'fileLink' : fileLinkDict,
                'recentReadUser' : recentReadUser
            }
            
            notices[idx] = academic
            testList = testList[6:]
            idx += 1
    
    return notices