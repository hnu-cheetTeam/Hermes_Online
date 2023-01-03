from fastapi import APIRouter, Depends
from bson.objectid import ObjectId
from serializers.userSerializers import userResponseEntity

from db import database
from db import schemas
import oauth2

router = APIRouter()
# ========================================================================================
# Main View

@router.get('/recentpost', response_model=schemas.UserPosts)
def read_recentPost(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(database.User.find_one({'_id': ObjectId(str(user_id))}))
    print("User Name :  %s  \nUser Email :  %s  \nUser Recent Post: %s"%(user["name"], user["email"], user["recentpost"]))
    return {"status": "success", "user": user}

# ========================================================================================
# MyPage View

@router.get('/info', response_model=schemas.UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(database.User.find_one({'_id': ObjectId(str(user_id))}))
    return {"status": "success", "user": user}

@router.get('/edit')
def editUserInfo():
    pass

# ========================================================================================
# Setting View
@router.post('/kw_regist')
def regist_Keyword(keywords:str, user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(database.User.find_one({'_id': ObjectId(str(user_id))}))
    user["keywords"] += keywords
    return {"status": "success", "user": user}

@router.get('/kw_read', response_model=schemas.UserKeywords)
def read_Keyword(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(database.User.find_one({'_id': ObjectId(str(user_id))}))
    print(user["keywords"])
    return {"status": "success", "user": user}

@router.post('/kw_delete')
def delete_Keyword():
    pass