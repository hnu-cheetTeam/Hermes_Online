# import os
# import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config import settings
from auth import router as auth_router
from user import router as user_router
# import routers.auth, routers.user
from crud.crud_user import (createAccount, createSuperAccount)
from data import Academic_Notice, Job_Notice, Notice, Scholarship_Notice
from db.database import (db, setAcademic, setJob, setNotice, setScholarship)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, tags=['Auth'], prefix='/api/auth')
app.include_router(user_router, tags=['Users'], prefix='/api/users')

# ========================================================================================
# Root path
@app.get('/')
@app.get('/main')
def mainView():
    return "FEVER Time"

# ========================================================================================
# Main View
# - Login Feature
# - Logout Feature
# - RealTime post
# - recent post

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