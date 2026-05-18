import sqlite3

DB_FILE = "simple.db"
SQL_FILE = "simple_database.sql"

with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    with open(SQL_FILE, "r", encoding="utf-8") as f:
        sql_script = f.read()
    cursor.executescript(sql_script)
    conn.commit()

    cursor.execute(
        "SELECT c.name, o.product, o.amount, o.order_date "
        "FROM customers c "
        "JOIN orders o ON c.id = o.customer_id "
        "ORDER BY c.id"
    )
    rows = cursor.fetchall()

print(f"Created {DB_FILE} and loaded data from {SQL_FILE}.\n")
print("Orders:")
for name, product, amount, order_date in rows:
    print(f"{name}: {product} - {amount} EUR on {order_date}")
