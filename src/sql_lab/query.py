import os
import logging
import mysql.connector


DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBNAME = os.getenv("DBNAME")

logging.basicConfig(level=logging.INFO)

def get_data_by_group(value):
    """Return rows where the group column matches value."""
    logging.info("Getting data by group")

    connection = mysql.connector.connect(
        host=DBHOST,
        user=DBUSER,
        password=DBPASS,
        database=DBNAME
    )

    cursor = connection.cursor()

    query = "SELECT * FROM mock WHERE `group` = %s"
    cursor.execute(query, (value,))

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results

def get_group_counts(groupby):
    """Count rows grouped by a selected column."""
    logging.info("Getting group counts")

    columns = {
        "id": "`id`",
        "group": "`group`",
        "last_name": "`last_name`",
        "age": "`age`",
        "email": "`email`",
        "city": "`city`"
    }

    if groupby not in columns:
        raise ValueError("Invalid column name")

    column = columns[groupby]

    connection = mysql.connector.connect(
        host=DBHOST,
        user=DBUSER,
        password=DBPASS,
        database=DBNAME
    )

    cursor = connection.cursor()

    query = f"SELECT {column}, COUNT(*) FROM mock GROUP BY {column}"
    cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results

def main():
    """Run example database queries."""
    group_data = get_data_by_group("Blue")
    print("Blue group:")
    print(group_data)

    counts = get_group_counts("group")
    print("Group counts:")
    print(counts)


if __name__ == "__main__":
    main()
