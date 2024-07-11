from sqlalchemy import select

from database import session_maker


class ClientsDAO:
    @classmethod
    async def get_all(cls, model):
        async with session_maker() as session:
            query = select(model)
            result = session.execute(query)
            return result.scalars()