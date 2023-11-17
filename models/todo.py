from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from services.database import Base


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    parent_id: Mapped[int] = mapped_column(default=None)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    priority: Mapped[int] = mapped_column(default=0)
    completed: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=True)

    # owner = relationship("User", back_populates="todos")
