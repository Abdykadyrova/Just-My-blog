from django.db import models
class Todo(models.Model):
    todo_name = models.CharField(max_length=300)
# Create your models here.


#модель таблицы blog_country
class Country(models.Model):
    country_name = models.CharField(max_length=300)

    class Meta:
        db_table ="blog_country"