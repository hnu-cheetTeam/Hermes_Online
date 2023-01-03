import os
import sys
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
