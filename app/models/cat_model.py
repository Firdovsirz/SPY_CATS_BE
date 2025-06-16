from app.db.session import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Numeric

class Cat(Base):
    __tablename__ = "cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    years_experience = Column(Integer, nullable=False)
    breed = Column(String, nullable=False)
    salary = Column(Numeric(10, 2), nullable=False)

    missions = relationship("Mission", back_populates="cat", cascade="all, delete-orphan")