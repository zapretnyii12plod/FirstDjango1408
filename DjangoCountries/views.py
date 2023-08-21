from django.http import HttpResponse
from django.shortcuts import render
from DjangoCountries.models import Country, Language
import json
import string as st
import math

# Create your views here.

def bd(request):
 with open("country.json", "r") as read_file:
  countries = json.loads(read_file.read())
# for country in countries:
#  country_ = Country(name=country['country'])
#  country_.save()

# languages_list = set();
# for country in countries:
#  for language in country['languages']:
#   languages_list.add(language)
# languages = sorted(list(languages_list))
# for language in languages:
#  language_ = Language(name=language)
#  language_.save()

# countries_ = Country.objects.all()
# languages_ = Language.objects.all()
# for country_ in countries_:
#  for country in countries:
#   if (country['country'] == country_.name):
#    languages = country['languages']
#    for language in languages:
#     for language_ in languages_:
#      if (language == language_.name):
#       country_.languages.add(language_)
#  country_.save()

 return HttpResponse('Ok')

def root(request):
 context = {}

 return render(request, 'country-index.html', context)

def countries_list(request, p):
# with open("country.json", "r") as read_file:
#  countries = json.loads(read_file.read())
# country_list = [];
# for country in countries:
#  country_list.append(country['country'])
 country_list = Country.objects.all()
 pages = math.ceil(len(country_list) / 10)
 alphabet = list(st.ascii_uppercase)
 country_list = country_list[(p-1)*10:p*10]
 context = {'countries':country_list, 'alphabet':alphabet, 'pages':range(1, pages+1)}
 return render(request, 'countries-list.html', context)

def country(request, id):
# with open("country.json", "r") as read_file:
#  countries = json.loads(read_file.read())
# country_list = [];
# for country in countries:
#  country_list.append(country['country'])
# for idx, country in enumerate(country_list, start=1):
#  if idx == id:
 country = Country.objects.get(id=id)
 languages = country.languages.all()
 context = {"country": country, "languages": languages}

 return render(request, 'country.html', context)

def countries_by_letter(request, letter):
# with open("country.json", "r") as read_file:
#  countries = json.loads(read_file.read())
# country_list = []
# for country in countries:
#  country_list.append(country['country'])
# country_list = list(enumerate(country_list, start=1))
 country_out_list = []
 country_list = Country.objects.all()
 for country in country_list:
  if country.name[0] == letter:
   country_out_list.append((country.id, country.name))
 alphabet = list(st.ascii_uppercase)
 context = {'countries':country_out_list, 'alphabet':alphabet}
 return render(request, 'countries_by_letter.html', context)

def languages_list(request):
# with open("country.json", "r") as read_file:
#  countries = json.loads(read_file.read())
# languages_list = set();
# for country in countries:
#  for language in country['languages']:
#   languages_list.add(language)
 languages = Language.objects.all()
 context = {'languages':languages}
 return render(request, 'languages-list.html', context)

def language(request, id):
# with open("country.json", "r") as read_file:
#  countries = json.loads(read_file.read())
# languages_list = set();
# for country in countries:
#  for language in country['languages']:
#   languages_list.add(language)
# languages_list = sorted(list(languages_list))
# for idx, language in enumerate(languages_list, start=1):
#  if idx == id:
#   our_language = language
# our_countries = []
# for country in countries:
#  for language in country['languages']:
#   if our_language == language:
#    our_countries.append(country['country'])

 countries = set()

 language = Language.objects.get(id=id)
 country_list = Country.objects.all()
 for country in country_list:
  languages = country.languages.all()
  for language_ in languages:
   if (language_.name == language.name):
    countries.add(country.name)

 countries = sorted(list(countries))

 context = {"countries": countries, "language": language}

 return render(request, 'language.html', context)