from typing import List
from sqlalchemy.orm import Session
from models.user_address import UserAddress
from .base import BaseSQLAlchemyRepository

class UserAddressRepository(BaseSQLAlchemyRepository[UserAddress]):

    def __init__(self, db: Session):
        super().__init__(db, UserAddress)

    def get_addresses_by_user_id(self, user_id: int) -> List[UserAddress]:
        return self.db.query(UserAddress).filter(UserAddress.user_id == user_id).all()

    def get_address_by_id_and_user_id(self, address_id: int, user_id: int) -> UserAddress:
        return self.db.query(UserAddress).filter(UserAddress.id == address_id, UserAddress.user_id == user_id).first()
