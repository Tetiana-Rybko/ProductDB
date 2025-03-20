from sqlalchemy_train.sql_queries.models import User, Role, Comment, News
from sqlalchemy_train.sql_queries.db_connection import DBConnection
from sqlalchemy_train.sql_queries import engine


with DBConnection(engine) as session:
    ...
