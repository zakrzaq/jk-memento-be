from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from services.database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    parent_id = Column(Integer, default=None)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer, default=0)
    # labels = Column()
    completed = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    owner = relationship("User", back_populates="todos")
