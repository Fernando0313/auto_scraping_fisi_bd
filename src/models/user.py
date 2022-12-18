import conexion_bd
from sqlalchemy import Column, types



class UserModel(conexion_bd.Base):
    __tablename__ = 'user'

    userId = Column(name='id', type_=types.Integer,
                   autoincrement=True, primary_key=True)

    userFirstName = Column(name='first_name', type_=types.Text)

    userLastName = Column(name='last_name', type_=types.Text)

    userName = Column(name='name', type_=types.Text)

    userPassword = Column(name='password', type_=types.Text)

    userEmail = Column(name='email', type_=types.Text)