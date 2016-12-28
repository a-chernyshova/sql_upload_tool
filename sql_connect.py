# -*- coding: utf-8 -*-
import mysql.connector

# запись в БД
#INSERT INTO `movie_test`.`actors` (`ID`, `NAME`, `AGE`) VALUES (11, 'Anthony Hopkins', 78);

cnx = mysql.connector.connect(user='manager', password='password',
                              host='127.0.0.1',
                              database='movie_test')
db_tables = {'actors': 'ID, name, age', 'movies': "ID, name, duration, year_release, genre",
            "reviews": "ID, text, movie_ID, author, mark", "a_m": "ID, movie_id, actor_id"}

def insert_into_table(tablename, data_list):
    cursor = cnx.cursor()
    dbtask = ("INSERT INTO " + tablename + "(" + db_tables[tablename] +")" + " VALUES (" + data_list + ")")
    print (dbtask)
    cursor.execute(dbtask)
    cnx.commit()
    cursor.close()

def close():
    cnx.close()

#write_to_db("actors", "12, 'man1', 12")
#close()