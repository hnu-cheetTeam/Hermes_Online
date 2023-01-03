def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "profileImg": user["profileImg"],
        "name": user["name"],
        "nickName": user["nickName"],
        "email": user["email"],
        "password": user["userPw"],
        "verified": user["verified"],
        "studentCode": user["studentCode"],
        "birth": user["birth"],
        "keywords": user["keywords"],
        "recentPost": user["recentPost"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"]
    }

def userResponseEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "profileImg": user["profileImg"],
        "name": user["name"],
        "nickName": user["nickName"],
        "email": user["email"],
        "password": user["userPw"],
        "studentCode": user["studentCode"],
        "birth": user["birth"],
        "keywords": user["keywords"],
        "recentPost": user["recentPost"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"]
    }

def embeddedUserResponse(user) -> dict:
    return {
        "id": str(user["_id"]),
        "profileImg": user["profileImg"],
        "name": user["name"],
        "keywords": user["keywords"],
        "recentPost": user["recentPost"]
    }

def userListEntity(users) -> list:
    return [userEntity(user) for user in users]