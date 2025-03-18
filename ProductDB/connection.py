from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


sqla_engine = create_engine(
    url="sqlite:///example.db",
    echo=True,
    echo_pool=True,
)
#=======================================================================================
Session = sessionmaker(bind=sqla_engine)
session = Session()