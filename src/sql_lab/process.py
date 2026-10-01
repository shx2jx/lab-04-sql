import os
import logging
import pandas as pd
import mysql.connector


DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBNAME = os.getenv("DBNAME")

logging.basicConfig(level=logging.INFO)


def read_data(filename):
    """Read CSV file into pandas DataFrame."""
    logging.info("Reading data")
    data = pd.read_csv(filename)
    return data


def clean_data(data):
    """Remove rows with missing values."""
    logging.info("Cleaning data")
    data = data.dropna()
    return data


def load_data(data, table):
    """Create a MySQL table and upload the DataFrame."""
    logging.info("Loading data")

    try:
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME
        )

        cursor = connection.cursor()

        create_query = """
        CREATE TABLE IF NOT EXISTS mock (
            id BIGINT PRIMARY KEY,
            `group` VARCHAR(255),
            last_name VARCHAR(255),
            age BIGINT,
            email VARCHAR(255),
            city VARCHAR(255)
        )
        """

        cursor.execute(create_query)

        insert_query = """
        INSERT INTO mock
        (id, `group`, last_name, age, email, city)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        for row in data.itertuples(index=False, name=None):
            cursor.execute(insert_query, row)

        connection.commit()
        logging.info("Data loaded successfully")

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)

    finally:
        if "cursor" in locals():
            cursor.close()

        if "connection" in locals() and connection.is_connected():
            connection.close()


def main():
    """Run the data processing and upload pipeline."""
    data = read_data("MOCK_DATA.csv")
    data = clean_data(data)
    load_data(data, "mock")


if __name__ == "__main__":
    main()
