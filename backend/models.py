from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy import String


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(unique=True)
    