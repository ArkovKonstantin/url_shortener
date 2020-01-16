import aiopg.sa
from sqlalchemy import (
    MetaData, Table, Column, String, DateTime
)
from datetime import datetime as dt

meta = MetaData()

url = Table(
    'url', meta,

    Column('key', String(24), primary_key=True),
    Column('original_url', String(200), nullable=False),
    Column('creation_date', DateTime, default=dt.utcnow())
)


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port']
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
