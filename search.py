def search(cur):
    cur.execute('SELECT email FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    print(row)