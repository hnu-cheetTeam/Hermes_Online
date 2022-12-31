import os
import sys
import json
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

@app.get('/')
def mainView():
    # print(db['academic'].find_one())
    return {"message": "hi hello"}

@app.get('/auth/login')
def login():
    pass

@app.get('/auth/logout')
def logout():
    pass

@app.get('/main/realtimepost')
def update_realtimepost():
    pass

@app.get('/main/recentpost')
def recentPost():
    pass

@app.get('/academic')
def academic():
    # setAcademic()
    res = db['academic'].find_one()
    print(type(res))
    return json.dumps(res)

@app.get('/notice')
def notice():
    # setNotice()
    return {"message": "Academic Complete"}

@app.get('/scholarship')
def scholarship():
    # setScholarship()
    return {"Contents": "test"}

@app.get('/job')
def job():
    # setJob()
    return {'Contents': "test"}


if __name__=='__main__':
    app.run(debug=True)