import mysql.connector
import sys

try:
    conn = mysql.connector.connect(
        host="host.docker.internal",
        port=3307,
        user="root",
        password="root",
        database="sales_dw"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM bronze_superstore_raw;")
    result = cursor.fetchone()[0]

    if result > 0:
        print("Data exists:", result)
        sys.exit(0)
    else:
        print("No data found")
        sys.exit(1)

except Exception as e:
    print("Error:", e)
    sys.exit(1)