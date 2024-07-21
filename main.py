from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from dependencies import get_db, get_current_user
from schemas.user_address import UserAddressDetail, UserAddressList
from services.user_address_service import UserAddressService
from repositories.user_address_repository import UserAddressRepository
from models.user import User

app = FastAPI()

def get_user_address_service(db: Session = Depends(get_db)) -> UserAddressService:
    user_address_repository = UserAddressRepository(db)
    return UserAddressService(user_address_repository)

@app.get("/addresses", response_model=List[UserAddressList])
def list_user_addresses(
    current_user: User = Depends(get_current_user),
    user_address_service: UserAddressService = Depends(get_user_address_service)
):
    return user_address_service.get_user_addresses(current_user.id)

@app.get("/addresses/{address_id}", response_model=UserAddressDetail)
def get_user_address(
    address_id: int,
    current_user: User = Depends(get_current_user),
    user_address_service: UserAddressService = Depends(get_user_address_service)
):
    return user_address_service.get_user_address(address_id, current_user.id)
