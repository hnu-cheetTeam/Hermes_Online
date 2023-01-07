from datetime import datetime
from pydantic import BaseModel, EmailStr, constr
from bson.objectid import ObjectId

class UserBaseSchema(BaseModel):
    name: str
    email: str
    photo: str
    role: str or None = None
    created_at: datetime or None = None
    updated_at: datetime or None = None
    keywords: str
    class Config:
        orm_mode = True

class UserInfoBaseSchema(BaseModel):
    keywords: str
    class Config:
        orm_mode = True

class UserPostBaseSchema(BaseModel):
    recentpost: str
    class Config:
        orm_mode = True

class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    verified: bool = False


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponseSchema(UserBaseSchema):
    id: str
    pass

class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema

class UserResponseKeywords(UserInfoBaseSchema):
    id: str

class UserKeywords(BaseModel):
    status: str
    user: UserResponseKeywords