from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Air(models.Model):
    cityname = models.CharField(db_column='cityName', max_length=255)  # Field name made lowercase.
    citynameeng = models.CharField(db_column='cityNameEng', max_length=255)  # Field name made lowercase.
    datatime = models.DateTimeField(db_column='dataTime')  # Field name made lowercase.
    so2value = models.CharField(db_column='so2Value', max_length=10)  # Field name made lowercase.
    covalue = models.CharField(db_column='coValue', max_length=10)  # Field name made lowercase.
    o3value = models.CharField(db_column='o3Value', max_length=10)  # Field name made lowercase.
    no2value = models.CharField(db_column='no2Value', max_length=10)  # Field name made lowercase.
    pm10value = models.CharField(db_column='pm10Value', max_length=10)  # Field name made lowercase.
    pm25value = models.CharField(db_column='pm25Value', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'air'


class Corona19(models.Model):
    createdt = models.DateTimeField()
    statedt = models.DateField()
    statetime = models.TimeField()
    decidecnt = models.CharField(max_length=255)
    carecnt = models.CharField(max_length=255)
    clearcnt = models.CharField(max_length=255)
    deathcnt = models.CharField(max_length=255)
    examcnt = models.CharField(db_column='examCnt', max_length=255)  # Field name made lowercase.
    resutlnegcnt = models.CharField(max_length=255)
    accdefrate = models.CharField(max_length=255)
    accexamcnt = models.CharField(db_column='accExamCnt', max_length=255)  # Field name made lowercase.
    accexamcompcnt = models.CharField(db_column='accExamCompCnt', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'corona19'


class News(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    urltoimage = models.CharField(db_column='urlToImage', max_length=256, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=256)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'news'


class Weather(models.Model):
    basedate = models.DateField(db_column='baseDate')  # Field name made lowercase.
    basetime = models.TimeField(db_column='baseTime')  # Field name made lowercase.
    category = models.CharField(max_length=4)
    fcstdate = models.DateField(db_column='fcstDate')  # Field name made lowercase.
    fcsttime = models.TimeField(db_column='fcstTime')  # Field name made lowercase.
    fcstvalue = models.CharField(db_column='fcstValue', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nx = models.IntegerField()
    ny = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'weather'
