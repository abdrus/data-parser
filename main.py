from peewee import *
from datetime import *
from models import SearchContext, SearchRequest, db

db.connect()

# За кого болели больше - Испанию или Португалию?
dayOfMatch = '2018-06-15'
result1 = SearchRequest.select().where(SearchRequest.text.contains('испани'))
result2 = SearchRequest.select().where(SearchRequest.text.contains('порту'))
print('Запросов в день матча об Испании: ' + str(result1.count()))
print('Запросов в день матча об Португалии: ' + str(result2.count()))

# Сколько запросов со словом "билет" было в день матча Испания-Португалия
result3 = SearchRequest.select().where(SearchRequest.text.contains('билет'))
print("Запросов со словом 'билет' было в день матча Испания-Португалия: "+ str(result3.count()))

# Сколько людей хотели купить билет в день матча "Испания-Португалия"
contexts = [request.context.id for request in result3]
result4 = SearchRequest.select().where(SearchRequest.context.in_(contexts)).where(SearchRequest.text.contains('купить')).count()
print('Сколько людей хотели купить билет в день матча "Испания-Португалия": ' + str(result4))