#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
where name matches the argument and safe from MySQL injections!
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall() if state[1] == argv[4]]
