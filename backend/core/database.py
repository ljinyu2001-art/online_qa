from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = (
    "mysql+pymysql://root:123456@192.168.110.118:3306/online_qa?charset=utf8mb4"
)


engine = create_engine(
    DATABASE_URL,
    echo=True
)


SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base=declarative_base()


def get_db():

    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()