import mysql.connector
from mysql.connector import Error
from faker import Faker
import sys

Faker.seed(0)
fake = Faker()

create_people_sql = """
CREATE TABLE `people` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `city` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `country` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `phone_number` varchar(25) COLLATE utf8_unicode_ci NOT NULL, 
  `birthdate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
"""

def create_table(cursor, sql_statement):
    try:
        cursor.execute(sql_statement)
        print("Table created")
    except Exception as e:
        pass
        # print("Error creating table", e)
def populate_tables(cursor):
    cursor.execute("SELECT * FROM people;")
    if not cursor.fetchall():
            row = {}
            n = 0
            while n < 5:
                try:
                    n += 1
                    # define data to be inserted
                    row = [fake.first_name(), fake.last_name(), fake.email(),
                           fake.city(), fake.country(), fake.country_calling_code() + fake.msisdn(), fake.date_of_birth()]

                    add_person = ("INSERT INTO people "
                                   "(first_name, last_name, email, city, country, phone_number, birthdate)"
                                   "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                    data_person = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])

                    cursor.execute(add_person, data_person)
                    conn.commit()
                except Exception as e:
                    print(e)
                    # pass

try:
    db_host = sys.argv[1]
    db_name = sys.argv[2]
    db_user = sys.argv[3]
    db_password = sys.argv[4]

    conn = mysql.connector.connect(host=db_host, database=db_name,
                                   user=db_user, password=db_password)

    if conn.is_connected():
        cursor = conn.cursor()

        create_table(cursor, create_people_sql)
        populate_tables(cursor)

        print("Exiting...")

except Error as e :
    print ("error", e)
    pass
except Exception as e:
    print ("Unknown error %s", e)
finally:
    if(conn and conn.is_connected()):
        conn.commit()
        cursor.close()
        conn.close()