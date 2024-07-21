from pydantic import BaseModel

class UserAddressBase(BaseModel):
    title: str
    address_line: str
    city: str
    state: str
    postal_code: str
    country: str

class UserAddressCreate(UserAddressBase):
    pass

class UserAddressUpdate(UserAddressBase):
    pass

class UserAddressInDBBase(UserAddressBase):
    id: int

    class Config:
        orm_mode = True

class UserAddressInDB(UserAddressInDBBase):
    user_id: int

class UserAddressDetail(UserAddressInDBBase):
    pass

class UserAddressList(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True
