import os
import sys
from datetime import date
from fastapi import FastAPI
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pymongo import MongoClient
from data import Academic_Notice, Job_Notice, Notice, Scholarship_Notice

app = FastAPI()

client = MongoClient(host="localhost", port=27017)
db = client['dashboard_db']

def setAcademic():
    res = Academic_Notice.academic_notice()
    for key, val in res.items():
        print(f"key:{key} val:{val}")
        db["academic"].insert_one(val)

def setJob():
    res = Job_Notice.job_notice()
    for key, val in res.items():
        print(f"key:{key} val:{val}")
        db["job"].insert_one(val)

def setNotice():
    res = Notice.notice()
    for key, val in res.items():
        print(f"key:{key} val:{val}")
        db["notice"].insert_one(val)

def setScholarship():
    res = Scholarship_Notice.scholarship_notice()
    for key, val in res.items():
        print(f"key:{key} val:{val}")
        db["scholarship"].insert_one(val)

# ========================================================================================
# Root path
@app.get('/')
def mainView():
    return {"message": "hi hello"}

# ========================================================================================
# Main View
# - Login Feature
# - Logout Feature
# - RealTime post
# - recent post

def createAccount(profileImg_link:str, name:str, nickName:str, userId:str, userPw:str, studentCode:int, birth_year:int, birth_month:int, birth_day:int, email:str, keywords:list):
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
    return newUser

@app.post('/auth/login')
def login():
    pass

@app.post('/auth/logout')
def logout():
    pass

@app.get('/main/realtimepost')
def update_realtimepost():
    pass

@app.get('/main/recentpost')
def recentPost():
    pass

# ========================================================================================
# Academic Notice BoardView
@app.get('/academic')
def academic():
    post = list(db['academic'].find({}, {"_id":0, "class":1, "number":1, "title":1, "writer":1, "dateCreated":1, "postLink":1, "fileName":1, "fileLink":1}))
    info = createAccount("dummy profileImgLink", "super", "Administrator", "super", "1234", "10000000", 2023, 1, 1, "aaaa@aaaa", [])
    db["user"].insert_one(info)
    print(info)
    return post

# ========================================================================================
# Notice BoardView
@app.get('/notice')
def notice():
    post = list(db['notice'].find({}, {"_id":0, "class":1, "number":1, "title":1, "writer":1, "dateCreated":1, "postLink":1, "fileName":1, "fileLink":1}))
    return post

# ========================================================================================
# Scholarship Notice BoardView
@app.get('/scholarship')
def scholarship():
    post = list(db['scholarship'].find({}, {"_id":0, "class":1, "number":1, "title":1, "writer":1, "dateCreated":1, "postLink":1, "fileName":1, "fileLink":1}))
    return post

# ========================================================================================
# Job Notice BoardView
@app.get('/job')
def job():
    post = list(db['job'].find({}, {"_id":0, "class":1, "number":1, "title":1, "writer":1, "dateCreated":1, "postLink":1, "fileName":1, "fileLink":1}))
    return post

# ========================================================================================
# MyPage View
@app.get('/user/info')
def readUserInfo():
    pass

@app.get('/user/edit')
def editUserInfo():
    pass

# ========================================================================================
# Setting View
@app.post('/user/kw_regist')
def regist_Keyword():
    pass

@app.get('/user/kw_read')
def regist_Keyword():
    pass

@app.post('/user/kw_delete')
def regist_Keyword():
    pass

if __name__=='__main__':
    app.run(debug=True)