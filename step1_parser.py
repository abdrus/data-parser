from peewee import *
from datetime import *
import progressbar

db = SqliteDatabase('databases/initial.db')
logfile = 'logs/football.dms'
counter = 0

def log_length(logfile):
    count = 0;
    with open(logfile) as file:
        next(file)
        for line in file: count += 1
    return count

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

db.connect()
db.create_tables([SearchContext, SearchRequest])

print('Количество строк в лог-файле ' + str(log_length(logfile))+'\n')

bar = progressbar.ProgressBar(maxval=log_length(logfile), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

with open(logfile) as file:
    next(file)
    for line in file:
        list = line.split()
        reqDate = list[-2:-1][0]
        reqTime = list[-1:][0]
        reqAsList = list[:-2]
        reqAsString = ' '.join(reqAsList);

        context = SearchContext()
        context.save()

        for listItem in reqAsList:
            request = SearchRequest(
                text=listItem,
                date=datetime.strptime(reqDate, '%Y-%m-%d'),
                time=datetime.strptime(reqTime, '%H:%M:%S'),
                context=context
            )
            request.save()

        counter += 1
        bar.update(counter)

bar.finish();
print('Формирование начальной БД завершено\n')