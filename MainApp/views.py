from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

# itemslist = [
#    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#    {"id": 7, "name": "Картофель фри" ,"quantity":0},
#    {"id": 8, "name": "Кепка" ,"quantity":124},
# ]

# Create your views here.
def root_old(request):
 text = '<h1>"Изучаем django"</h1>'
 text += '<strong>Автор</strong>: <i>Кантёпкин Д.А.</i>'
 return HttpResponse(text)

def root(request):
 context = {
  "name": "Petrov Ivan Nikolaevich",
  "email": "my_mail@mail.ru"
 }
 return render(request, 'index.html', context)

def about(request):
  user = {'Имя': 'Денис', 
          'Отчество': 'Кантёпкин',
          'Фамилия': 'Иванов',
          'Телефон': '8-923-600-01-02',
          'email': 'vasya@mail.ru'}
  text = "<div><a href='/'>Home</a> > <a href='/about'>About</a></div>"
  text += "<br>"
  for idx, str_ in user.items():
   text += idx + ': ' + str_ + '<br/>'
  text += "<br>"
  text += "<div>/ <a href='/'>Home</a> / <a href='/items'>Items</a> / <a href='/about'>About</a> /</div>"
  return HttpResponse(text)

def item(request, id):
#  for item in itemslist:
#   if (item['id'] == id):
#    context = dict(item)
 try:
  one_item = Item.objects.get(id=id)
  colors = one_item.colors.all()
  #one_item.description = 'Armored car is not included'
  #one_item.save()
  context = {'id':one_item.id, 'name':one_item.name, 'brand':one_item.brand, 'quantity':one_item.count, 'colors':colors}
  return render(request, "item.html", context)
 except ObjectDoesNotExist:
  text = "Good with id "+str(id)+" not found"
  return HttpResponseNotFound(text)

def items(request):
#  text = "<ol>"
#  for it in itemslist:
#   text += "<li>Number: "+str(it['id'])+ " Name: <a href='/item/"+str(it['id'])+"'>"+str(it['name'])+"</a>, Quantity: "+str(it['quantity'])+"</li>"
#  text += "</ol>" 
#  return HttpResponse(text)
 itemslist = Item.objects.all()
 context = {
  "items": itemslist
 }
 return render(request, "items-list.html", context)