import asyncio
from sqlalchemy import insert, select
from sqlalchemy.exc import NoResultFound
from models import Users, UserOffice, async_session_factory


class DBExplore:
    async def insert_user(self, user_id: int, ref_id: int | None = None) -> bool:
        try:
            async with async_session_factory() as session:
                any_user = Users(user_id=user_id, ref_id=ref_id)
                session.add(any_user.id)
                await session.commit()
                return True
        except Exception:
            return False

    async def add_office(self, user_id: int, wb_token: str, name_office: str) -> bool:
        try:
            async with async_session_factory() as session:
                any_office = UserOffice(
                    wb_token=wb_token, name_office=name_office, user_id=user_id
                )
                session.add(any_office)
                await session.commit()
        except Exception:
            return False

    async def get_user_data(self, user_id: int) -> Users | bool:
        try:
            async with async_session_factory() as session:
                stmt = select(Users).where(Users.user_id == user_id)
                user_data = await session.scalars(stmt)
                return user_data.one()
        except NoResultFound:
            return False


async def async_conn():
    db = DBExplore()
    user = await db.get_user_data(4412)
    print(user.user_id)


asyncio.run(async_conn())
