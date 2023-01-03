import os
import sys
from datetime import date
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from db.database import db

def createAccount(profileImg_link:str, name:str, nickName:str, userId:str, userPw:str, studentCode:int, birth_year:int, birth_month:int, birth_day:int, email:str, keywords:list, recentPost:list):
    newUser = {}
    userBirth = date(birth_year, birth_month, birth_day)
    newUser['profileImg']=profileImg_link
    newUser['name']=name
    newUser['nickName']=nickName
    newUser['userId']=userId
    newUser['userPw']=userPw
    newUser['studentCode']=studentCode
    newUser['birth']=userBirth.isoformat()
    newUser['email']=email
    newUser['keywords']=keywords
    newUser['recentPost']=recentPost
    db["user"].insert_one(newUser)

def createSuperAccount():
    createAccount("dummy profileImgLink", "super", "Administrator", "super", "1234", "10000000", 2023, 1, 1, "aaaa@aaaa", [], [])

# def readAccount():
#     pass

# def readAccount_all():
#     pass

# def updateAccount():
#     pass

# def deleteAccount():
#     pass

# def deleteAccount_all():
#     pass