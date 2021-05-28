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

def insert(key, datas):
    with connection:
        with connection.cursor() as cursor:
            if key == 'corona19':
                sql = 'INSERT INTO `corona19`(`createdt`, `statedt`,\
                `statetime`, `decidecnt`, `carecnt`, `clearcnt`,\
                `deathcnt`, `examCnt`, `resutlnegcnt`, `accdefrate`, \
                `accExamCnt`, `accExamCompCnt`) \
                VALUES("{}", "{}", "{}", {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(datas[0], datas[1], datas[2], 
                                                                                     datas[3], datas[4], datas[5], 
                                                                                     datas[6], datas[7], datas[8], 
                                                                                     datas[9], datas[10], datas[11])
                cursor.execute(sql)
            elif key == 'weather':
                print(datas)
                for i in range(10):
                    sql = 'INSERT INTO `weather` (`baseDate`, `baseTime`, \
                    `category`, `fcstDate`, `fcstTime`, `fcstValue`, \
                    `nx`, `ny`) VALUES ("{}", "{}", "{}", "{}", "{}", {}, {}, {})'.format(datas[i][0], datas[i][1], datas[i][2], 
                                                                                            datas[i][3], datas[i][4], datas[i][5], 
                                                                                            datas[i][6], datas[i][7])
                    cursor.execute(sql)
            # elif key == 'news':
            #     sql = 
            
            
        connection.commit()
        
        
# scrapping data insert
# def insert(scp_result):
#     with connection:
#         with connection.cursor() as cursor:
#             # Create a new record
#             sql = "INSERT INTO `news_headlines`(`title`, `date_time`) VALUES (%s, NOW())"
#             for i in scp_result:
#                 cursor.execute(sql, i)

#         # connection is not autocommit by default. So you must commit to save
#         # your changes.
#         connection.commit()

#     return 1


def select():
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `title` FROM `news_headlines`"
        cursor.execute(sql)
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        print(df)

    return df