from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, Text
from sqlalchemy.orm import relationship
from app.db.session import Base

class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(Integer, ForeignKey("cats.id", ondelete="SET NULL"), nullable=True)
    complete = Column(Boolean, default=False, nullable=False)

    cat = relationship("Cat", back_populates="missions", passive_deletes=True)
    targets = relationship("Target", cascade="all, delete-orphan", back_populates="mission")


class Target(Base):
    __tablename__ = "targets"

    id = Column(Integer, primary_key=True, index=True)
    mission_id = Column(Integer, ForeignKey("missions.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    notes = Column(Text, nullable=True)
    complete = Column(Boolean, default=False, nullable=False)

    mission = relationship("Mission", back_populates="targets")