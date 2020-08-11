import sqlite3

conn=sqlite3.connect("auth.db")
cur=conn.cursor()
donnee=(1 , "ged","ged",'mail')
cur.execute("create table auth (id integer ,login  ,password ,email)")
cur.execute("insert into auth (id ,login ,password ,email) values( ?,?,?,?)",donnee)
conn.commit()
cur.close()
conn.close()