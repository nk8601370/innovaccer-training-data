from sqlalchemy import create_engine

db_string = "postgresql://postgres:postgres@127.0.0.1:5432/flasksample"

db = create_engine(db_string)

#db.execute("insert into users values ('rohit','rohit@xyz.com','okayrohit') ")

#db.execute("update users set password='newpass' where name='rohit'")

db.execute("delete from users where name='rohit'")






result = db.execute("select * from users")
for i in result:
    print(i)
