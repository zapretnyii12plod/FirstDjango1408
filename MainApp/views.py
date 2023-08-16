from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

itemslist = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

# Create your views here.
def root(request):
 text = '<h1>"Изучаем django"</h1>'
 text += '<strong>Автор</strong>: <i>Кантёпкин Д.А.</i>'
 return HttpResponse(text)

def about(request):
  user = {'Имя': 'Денис', 
          'Отчество': 'Кантёпкин',
          'Фамилия': 'Иванов',
          'Телефон': '8-923-600-01-02',
          'email': 'vasya@mail.ru'}
  text = ''
  for idx, str_ in user.items():
   text += idx + ': ' + str_ + '<br/>' 
  return HttpResponse(text)

def item(request, id):
 found = False
 for it in itemslist:
  if (it['id'] == id):
   text = "Name: "+str(it['name'])+", Quantity: "+str(it['quantity'])
   found = True
 if (found):
  return HttpResponse(text)
 else:
  text = "Good with id "+str(id)+" not found"
 return HttpResponseNotFound(text)

def items(request):
 text = "<ul>"
 for it in itemslist:
  text += "<li>Number: "+str(it['id'])+ " Name: <a href='/item/"+str(it['id'])+"'>"+str(it['name'])+"</a>, Quantity: "+str(it['quantity'])+"</li>"
 text += "</ul>" 
 return HttpResponse(text)
