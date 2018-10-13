import sqlite3

global db, cursor
db = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursor = db.cursor()


def intodb(a, b):
    cursor.execute('''INSERT INTO trad_dict (ar,eng) VALUES(?,?)''', (a, b))
    db.commit()


def verf(a):
    m = a[0].upper() + a[1:].lower()
    A = 'ar'
    B = 'eng'
    cursor.execute('''SELECT {}, {}  FROM trad_dict'''.format(A, B))
    all = cursor.fetchall()
    w = []
    for i in all:
        if i[0][:len(m)] == m:
            z = '{} : {}'.format(i[0], i[1])
            w.append(z)

    return w
