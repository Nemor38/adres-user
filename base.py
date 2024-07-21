from sqlalchemy.orm import Session

class BaseSQLAlchemyRepository:
    def __init__(self, db: Session, model):
        self.db = db
        self.model = model

    def add(self, obj):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get(self, id: int):
        return self.db.query(self.model).filter(self.model.id == id).first()

    def delete(self, id: int):
        obj = self.get(id)
        if obj:
            self.db.delete(obj)
            self.db.commit()
        return obj
