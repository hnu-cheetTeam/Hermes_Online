# import os
# import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config import settings
from auth import router as auth_router
from user import router as user_router
from crud.crud_user import (createAccount, createSuperAccount)
from data import Academic_Notice, Job_Notice, Notice, Scholarship_Notice
from db.database import (db, set_AllRecentPost, set_RecentAcademic, set_RecentJob, set_RecentNotice, set_RecentScholarship)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, tags=['Auth'], prefix='/auth')
app.include_router(user_router, tags=['Users'], prefix='/user')

# ========================================================================================
# Root path
@app.get('/')
@app.get('/main')
def mainView():
    # set_AllRecentPost()
    # set_RecentAcademic()
    # set_RecentScholarship()
    # set_RecentJob()
    # set_RecentNotice()
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

# ========================================================================================
# Academic Notice BoardView
@app.get('/main/academic')
def academic():
    post = list(db['academic'].find({}, {"_id":0, "class":1, "number":1, "title":1, "writer":1, "dateCreated":1, "postLink":1, "fileName":1, "fileLink":1}))
    return post

# ========================================================================================
# Notice BoardView
@app.get('/main/notice')
def notice():
    post = list(db['notice'].find({}, {"_id":0, "class":1, "number":1, "title":1, "writer":1, "dateCreated":1, "postLink":1, "fileName":1, "fileLink":1}))
    return post

# ========================================================================================
# Scholarship Notice BoardView
@app.get('/main/scholarship')
def scholarship():
    post = list(db['scholarship'].find({}, {"_id":0, "class":1, "number":1, "title":1, "writer":1, "dateCreated":1, "postLink":1, "fileName":1, "fileLink":1}))
    return post

# ========================================================================================
# Job Notice BoardView
@app.get('/main/job')
def job():
    post = list(db['job'].find({}, {"_id":0, "class":1, "number":1, "title":1, "writer":1, "dateCreated":1, "postLink":1, "fileName":1, "fileLink":1}))
    return post

if __name__=='__main__':
    app.run(debug=True)