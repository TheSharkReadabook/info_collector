import database as database
# import corona19 as corona19
# import weather as weather
# import air as air
import news as news

# corona19 = corona19.corona19()

# database.insert('corona19', corona19)

# weather = weather.weather()

# database.insert('weather', weather)

# air = air.air()

# print(air)

# database.insert('air', air)

news = news.news()

print(news)

database.insert('news', news)
