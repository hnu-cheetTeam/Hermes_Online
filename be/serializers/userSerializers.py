def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "photo": user["photo"],
        "verified": user["verified"],
        "password": user["password"],
    }


def userResponseEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "photo": user["photo"],
    }


def embeddedUserResponse(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "photo": user["photo"]
    }

def userListEntity(users) -> list:
    return [userEntity(user) for user in users]