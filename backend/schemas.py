from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class UserBase(BaseSchema):
    name: str
    email: str

class UserResponse(UserBase):
    id: int