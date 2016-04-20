
class

def save_data(name,nfc,username,):
    conn = sqlite3.connect('nfcdatabase.db')
    cursor = conn.execute("SELECT name, nfc, username from users")
    aa=1
    for row in cursor:
        if row[0] == name:
            aa=2
            break
        if row[1] == nfc:
            aa=2
        if row[3] == username
            aa==2
            break
    if aa == 1:
            conn.execute("insert into users (name,nfc,username) values (?, ?, ?)",
                     (name,
                      nfc,
                      username))
            conn.commit()
            conn.close()
            return True
    else:
            return False


def get_data():
    conn = sqlite3.connect('nfcdatabase.db')
    cursor = conn.execute("SELECT name,name,email from users")
    data = [row for row in cursor]
    conn.close()
    return data
