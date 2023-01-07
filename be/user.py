from fastapi import APIRouter, Depends
from bson.objectid import ObjectId
from serializers.userSerializers import userResponseEntity, userDetailEntity

from db import database
from db import schemas
import oauth2

router = APIRouter()
# ========================================================================================
# Main View


# ========================================================================================
# MyPage View

@router.get('/info', response_model=schemas.UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(database.User.find_one({'_id': ObjectId(str(user_id))}))
    return {"status": "success", "user": user}

# @router.get('/info/edit')
# def editUserInfo():
#     pass

# ========================================================================================
# Setting View
@router.get('/create/keywords={keywords}')
def create_Keyword(keywords, user_id: str = Depends(oauth2.require_user)):
    user = database.User.find_one({'_id': ObjectId(str(user_id))})
    origin_keywords = user["keywords"]
    sep_keywords = keywords.split()
    origin_keywords += " "
    origin_keywords += " ".join(sep_keywords)

    database.User.update_one( {'_id': ObjectId(str(user_id))}, 
                                { "$set": {"keywords": origin_keywords}})

    print(origin_keywords)
    return {"Origin Keywords": origin_keywords, "Now Keywords": user["keywords"]}

@router.get('/read/keywords', response_model=schemas.UserKeywords)
def read_Keyword(user_id: str = Depends(oauth2.require_user)):
    user = userDetailEntity(database.User.find_one({'_id': ObjectId(str(user_id))}))
    print(str(user_id))
    print(user["keywords"])
    return {"status": "success", "user": user}

@router.get('/update/keywords={newkeywords}')
def update_Keyword(newkeywords:str, user_id: str = Depends(oauth2.require_user)):
    database.User.update_one( {'_id': ObjectId(str(user_id))}, 
                                { "$set": {"keywords": newkeywords}})
    user = database.User.find_one({'_id': ObjectId(str(user_id))})
    print(user)
    return {"New Keywords": newkeywords, "Now Keywords": user["keywords"]}
