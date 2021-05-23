import pymysql.cursors
import pandas as pd


# Connect to the database
connection = pymysql.connect(host='localhost',
                         user='infouser',
                         password='asd123',
                         database='infomations',
                         charset='utf8',
                        cursorclass=pymysql.cursors.DictCursor)
if connection:
    result = 'Mysql connection successed'


def db_insert(scp_result):
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `news_headlines`(`title`, `date_time`) VALUES (%s, NOW())"
            for i in scp_result:
                cursor.execute(sql, i)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    return 1


def db_select():
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `title` FROM `news_headlines`"
        cursor.execute(sql)
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        print(df)

    return df