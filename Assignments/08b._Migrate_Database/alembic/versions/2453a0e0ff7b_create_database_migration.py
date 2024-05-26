"""create database migration

Revision ID: 2453a0e0ff7b
Revises: 46efc71b4862
Create Date: 2024-05-04 14:23:04.135973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.sql import sqltypes

from sqlalchemy import create_engine, Table, Column, Integer, Unicode, MetaData, String, Text, update, and_, select, func, types, event
from dotenv import load_dotenv
import os
load_dotenv()
password = os.getenv("PASSWORD")

# revision identifiers, used by Alembic.
revision: str = '2453a0e0ff7b'
down_revision: Union[str, None] = '46efc71b4862'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


user = os.getenv("DB_USER", "")
password = os.getenv("DB_PASS", "")
host = os.getenv("DB_HOST", "")
db = os.getenv("DB_NAME", "")
new_db = os.getenv("DB_NAME_2", "")



exclude_tables = ['alembic_version']
def upgrade() -> None:
    source_engine = sa.create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")


    target_engine = sa.create_engine(f"mysql+pymysql://{user}:{password}@{host}/{new_db}")
    if not database_exists(target_engine.url):
        create_database(target_engine.url)
    
    source_metadata = MetaData()
    target_metadata = MetaData()

    source_conn = source_engine.connect()
    target_conn = target_engine.connect()

    source_metadata.reflect(bind=source_engine)

    for table in source_metadata.sorted_tables:
        if table.name not in exclude_tables:
            table.create(bind=target_engine)

    target_metadata.clear()
    target_metadata.reflect(bind=target_engine)

    for table in target_metadata.sorted_tables:
        src_table = source_metadata.tables[table.name]
        stmt = table.insert()
        for index, row in enumerate(source_conn.execute(src_table.select())):
            target_conn.execute(stmt.values(row))

    target_conn.commit()
    source_conn.close()
    target_conn.close()


def downgrade() -> None:
    pass
