from app.api.models import NoteSchema
from app.db import database, notes


async def post(payload: NoteSchema):
    query = notes.insert().values(
        title=payload.title, description=payload.description
    )
    return await database.execute(query=query)  # returns an ID


async def get(id: int):
    query = notes.select().where(id == notes.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = notes.select()
    return await database.fetch_all(query=query)
