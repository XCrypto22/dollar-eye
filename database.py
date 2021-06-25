import sqlite3


def create_table():
    conn = sqlite3.connect('qr.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS wallet (balance REAL)")
    conn.commit()
    conn.close()


def check_balance():
    conn = sqlite3.connect('qr.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM wallet")
    rows = cur.fetchall()
    conn.close()
    return rows


def credit(amnt):
    conn = sqlite3.connect('qr.db')
    cur = conn.cursor()
    cur.execute("UPDATE wallet SET balance = balance - ?",(amnt,))
    conn.commit()
    conn.close()

def deposit(amnt):
    conn = sqlite3.connect('qr.db')
    cur = conn.cursor()
    cur.execute("UPDATE wallet SET balance = balance + ?",(amnt,))
    conn.commit()
    conn.close()

def insert(amnt):
    conn = sqlite3.connect('qr.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO wallet(balance) VALUES (?)",(amnt,))
    conn.commit()
    conn.close()
