import os
import sys
from datetime import datetime
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pymongo import mongo_client
from config import settings
from data import Academic_Notice, Job_Notice, Notice, Scholarship_Notice

client = mongo_client.MongoClient(
    settings.DATABASE_URL, 
    serverSelectionTimeoutMS=5000)

try:
    conn = client.server_info()
    print(f'Connected to MongoDB {conn.get("version")}')
except Exception:
    print("Unable to connect to the MongoDB server.")

# db = client['dashboard_db']
db = client[settings.MONGO_INITDB_DATABASE]
User = db.user


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

def set_AllRecentPost():
    allPost = list(db['academic'].find({}, {"_id":0, "fileName":0, "fileLink":0}).limit(10))
    allPost += list(db['notice'].find({}, {"_id":0, "class":1, "number":1, "title":1, "writer":1, "dateCreated":1, "postLink":1, "fileName":1, "fileLink":1}).limit(10))
    allPost += list(db['scholarship'].find({}, {"_id":0, "class":1, "number":1, "title":1, "writer":1, "dateCreated":1, "postLink":1, "fileName":1, "fileLink":1}).limit(10))
    allPost += list(db['job'].find({}, {"_id":0, "class":1, "number":1, "title":1, "writer":1, "dateCreated":1, "postLink":1, "fileName":1, "fileLink":1}).limit(10))
    
    allPost = sorted(allPost, key=lambda x: datetime.strptime(x["dateCreated"].lstrip(), "%Y-%m-%d"), reverse=True)
    return allPost

def set_RecentAcademic():
    academic = list(db['academic'].find({}, {"_id":0, "fileName":0, "fileLink":0}).limit(10))
    academic = sorted(academic, key=lambda x: datetime.strptime(x["dateCreated"].lstrip(), "%Y-%m-%d"), reverse=True)
    print(academic)
    return academic

def set_RecentScholarship():
    scholarship = list(db['scholarship'].find({}, {"_id":0, "fileName":0, "fileLink":0}).limit(10))
    scholarship = sorted(scholarship, key=lambda x: datetime.strptime(x["dateCreated"].lstrip(), "%Y-%m-%d"), reverse=True)
    print(scholarship)
    return scholarship

def set_RecentNotice():
    notice = list(db['notice'].find({}, {"_id":0, "fileName":0, "fileLink":0}).limit(10))
    notice = sorted(notice, key=lambda x: datetime.strptime(x["dateCreated"].lstrip(), "%Y-%m-%d"), reverse=True)
    print(notice)
    return notice

def set_RecentJob():
    job = list(db['job'].find({}, {"_id":0, "fileName":0, "fileLink":0}).limit(10))
    job = sorted(job, key=lambda x: datetime.strptime(x["dateCreated"].lstrip(), "%Y-%m-%d"), reverse=True)
    print(job)
    return job
