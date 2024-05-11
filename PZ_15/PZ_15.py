# Приложение АПТЕКА для автоматизации работы аптечных пунктов. Таблица Лекарственные Средства должна содержать следующую информацию:
# Код, Название препарата, Применение, Количество, Цена, Страна-производитель.

import sqlite3 as sq
from medic import info_medicines

with sq.connect('pharmacy.db') as con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS medicines")
    cur.execute("CREATE TABLE IF NOT EXISTS medicines("
                "code INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT NOT NULL,"
                "usage TEXT NOT NULL,"
                "quantity INTEGER NOT NULL,"
                "price INTEGER NOT NULL,"
                "country TEXT NOT NULL)")
    
with sq.connect('pharmacy.db') as con:
    cur=con.cursor()
    cur.executemany("INSERT INTO medicines VALUES(?,?,?,?,?,?)", info_medicines)

with sq.connect('pharmacy.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM medicines WHERE country=='Россия'")
    result_1 = cur.fetchall()
    print(result_1)
"""with sq.connect('pharmacy.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM medicines WHERE name LIKE 'С%'")
    result_2 = cur.fetchall()
    print(result_2)"""
"""with sq.connect('pharmacy.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM medicines WHERE usage=='таблетки'")
    result_3 = cur.fetchall()
    print(result_3)"""
"""with sq.connect('pharmacy.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE medicines SET usage=='таблетки' WHERE country=='Германия'")
    cur.execute("SELECT * FROM medicines WHERE usage=='таблетки'")
    result_4=cur.fetchall()
    print(result_4)"""
"""with sq.connect('pharmacy.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE medicines SET country=='США' WHERE usage=='капли'")
    cur.execute("SELECT * FROM medicines WHERE country=='США'")
    result_5=cur.fetchall()
    print(result_5)"""
"""with sq.connect('pharmacy.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE medicines SET price==549 WHERE usage=='спрей' AND country=='Россия' ")
    cur.execute("SELECT * FROM medicines WHERE price>=500")
    result_6=cur.fetchall()
    print(result_6)"""
"""with sq.connect('pharmacy.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM medicines WHERE country=='Германия'")
    cur.execute("SELECT * FROM medicines")
    result_7=cur.fetchall()
    print(result_7)"""
"""with sq.connect('pharmacy.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM medicines WHERE quantity<=30")
    cur.execute("SELECT * FROM medicines")
    result_8=cur.fetchall()
    print(result_8)"""
"""with sq.connect('pharmacy.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM medicines WHERE name LIKE 'Г%'")
    cur.execute("SELECT * FROM medicines")
    result_9=cur.fetchall()
    print(result_9)"""
