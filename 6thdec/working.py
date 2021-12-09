from sqlalchemy import create_engine
from sqlalchemy.sql.schema import Column
from sqlalchemy import String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Integer

db_string = "postgresql://postgres:postgres@127.0.0.1:5432/flasksample"
db = create_engine(db_string)

base = declarative_base()


class users(base):
    __tablename__ = "users"
    #id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, primary_key = True, unique=False, nullable=False)
    password = Column(String, unique=True)
   
Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)


#Inserting the value
# players = users(name="Mayank",email="mayank@xyz.com",password="Manky123")
# session.add(players)
# session.commit()


#Updating the value
# players = session.query(users).filter(users.name=="Mayank").update({users.password:"wankhede123"})
# session.commit()

#deleting the value
players = session.query(users).filter(users.name=='gabbar').delete()

players = session.query(users)
for i in players:
    print("Player name is: "+i.name+". her/his email is "+i.email+". her/his password is"+i.password )