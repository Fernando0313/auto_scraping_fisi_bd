from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mssql://@localhost/agencia?driver=ODBC Driver 17 for SQL Server")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
