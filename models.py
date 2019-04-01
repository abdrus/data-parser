from peewee import *

db = SqliteDatabase('databases/initial.db')

class SearchContext(Model):
    class Meta:
        database = db

class SearchRequest(Model):
    text = CharField()
    date = DateField()
    time = TimeField()
    context = ForeignKeyField(SearchContext, backref='context')

    class Meta:
        database = db