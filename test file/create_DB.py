
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
sql = """create table skykiwi(
ID int,
WebLink varchar(255),
Title varchar(255),
Phone varchar(100),
RentAmount varchar(50),
Wechat varchat(100),
Content_Text varchar(500)
);
"""
cursor.execute(sql)
result = cursor.fetchall()
print(result)
conn.close()