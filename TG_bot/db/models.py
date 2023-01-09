from sqlalchemy import Column, Integer, String
from db import Base, engine

class Good(Base):
    __tablename__ = 'good'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    name = Column(String, nullable=False)
    quantity = Column(Integer)

    def __repr__(self):
        return f'Пользователь id={self.user_id}\nТовар id={self.id}\nНазвание товара={self.name}\nКоличество={self.quantity}'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
