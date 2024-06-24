import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy import MetaData, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from config_data import config


engine = config.db.engine
async_session_factory = async_sessionmaker(engine)

metadata: MetaData = MetaData()


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    feedbacks: Mapped[int] = mapped_column(default=60)
    signature: Mapped[str] = mapped_column(default="")
    all_feedbacks: Mapped[int] = mapped_column(default=60)
    ref_uid: Mapped["Users"] = mapped_column(ForeignKey("users.id"), nullable=True)


class UserOffice(Base):
    __tablename__ = "user_office"

    id: Mapped[int] = mapped_column(primary_key=True)
    wb_token: Mapped[str] = mapped_column(String(150), nullable=True)
    name_office: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped["Users"] = mapped_column(ForeignKey("users.id"))
