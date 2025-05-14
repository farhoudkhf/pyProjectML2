cur.execute("""
    INSERT INTO some_table (id, created_at, last_name)
    VALUES (%s, %s, %s);
    """,
    (10, datetime.date(2020, 11, 18), "O'Reilly"))