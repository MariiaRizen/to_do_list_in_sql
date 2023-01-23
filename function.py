from datetime import datetime
import sqlite3


con = sqlite3.connect('work_file.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = con.cursor()
cur.execute("CREATE TABLE to_do_list(id INTEGER, title, description, priority, due_date TIMESTAMP, done)")
cur.execute("""
    INSERT INTO to_do_list VALUES
        (1, "Buy book", "Psychological book", 3, datetime(2022, 9, 24, 16), True)
        (2, "Shopping", "Grosery shopping", 4, datetime(2022, 11, 1, 12, 37), False)
""")
cur.execute("""SELECT * FROM to_do_list""")
cur.execute("""UPDATE to_do_list
    SET priority = 1
    WHERE id = 1
""")
cur.execute("""DELETE FROM to_do_list WHERE id = 2""")
