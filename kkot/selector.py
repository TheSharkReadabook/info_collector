import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost', user='infouser',
                             password='asd123',
                             database='informations',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


def selector():
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `title`, `description`, `url`, `urlToImage` FROM `news`"
        cursor.execute(sql)
        result = cursor.fetchall()
    return result
