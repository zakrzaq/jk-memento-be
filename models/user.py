from sqlalchemy.orm import Mapped, mapped_column
from services.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str] = mapped_column()
    is_active: Mapped[bool] = mapped_column(default=True)

    # todos = relationship("Todo", back_populates="owner")
