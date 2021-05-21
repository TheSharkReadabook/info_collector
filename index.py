import scrapping as scrapping
import db as database
import kakaotalk as kkot

# url, select 등은 dictionary로 정리하기

scp_result = scrapping.scrapping()

# print(type(scp_result)) - <class 'list'>

db_result = database.db_insert(scp_result)

db_result = database.db_select()

kkot.kakaotalk(db_result['title'].to_json())
