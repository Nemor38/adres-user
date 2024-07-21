from typing import List
from repositories.user_address_repository import UserAddressRepository
from models.user_address import UserAddress
from fastapi import HTTPException

class UserAddressService:

    def __init__(self, user_address_repository: UserAddressRepository):
        self.user_address_repository = user_address_repository

    def get_user_addresses(self, user_id: int) -> List[UserAddress]:
        return self.user_address_repository.get_addresses_by_user_id(user_id)

    def get_user_address(self, address_id: int, user_id: int) -> UserAddress:
        address = self.user_address_repository.get_address_by_id_and_user_id(address_id, user_id)
        if not address:
            raise HTTPException(status_code=403, detail="Access forbidden")
        return address
