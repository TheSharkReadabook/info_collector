import scrapping as scrapping
import database as database
import kakaotalk as kkot
import corona19 as corona19
import weather as weather
import air as air
# url, select 등은 dictionary로 정리하기

# scp_result = scrapping.scrapping()

# db_result = database.db_insert(scp_result)

# db_result = database.db_select()

# kkot.kakaotalk(db_result['title'].to_json())

# ========= Available Functions ===========
# corona19 = corona19.corona19()

# database.insert('corona19', corona19)

# weather = weather.weather()

# database.insert('weather', weather)

air = air.air()

print(air)

database.insert('air', air)

