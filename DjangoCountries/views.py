from django.http import HttpResponse
from django.shortcuts import render
import json
import string as st
import math

# Create your views here.

def root(request):
 context = {}

 return render(request, 'country-index.html', context)

def countries_list(request, p):
 with open("country.json", "r") as read_file:
  countries = json.loads(read_file.read())
 country_list = [];
 for country in countries:
  country_list.append(country['country'])
 pages = math.ceil(len(country_list) / 10)
 alphabet = list(st.ascii_uppercase)
 country_list = list(enumerate(country_list, start=1))
 country_list = country_list[(p-1)*10:p*10]
 context = {'countries':country_list, 'alphabet':alphabet, 'pages':range(1, pages+1)}
 return render(request, 'countries-list.html', context)

def country(request, id):
 with open("country.json", "r") as read_file:
  countries = json.loads(read_file.read())
 country_list = [];
 for country in countries:
  country_list.append(country['country'])
 for idx, country in enumerate(country_list, start=1):
  if idx == id:
   our_country = country
 for country in countries:
  if our_country == country['country']:
   our_languages = country['languages']
 context = {"country": our_country, "languages": our_languages}

 return render(request, 'country.html', context)

def countries_by_letter(request, letter):
 with open("country.json", "r") as read_file:
  countries = json.loads(read_file.read())
 country_list = []
 for country in countries:
  country_list.append(country['country'])
 country_list = list(enumerate(country_list, start=1))
 country_out_list = []
 for idx, country in country_list:
  if country[0] == letter:
   country_out_list.append((idx, country))
 alphabet = list(st.ascii_uppercase)
 context = {'countries':country_out_list, 'alphabet':alphabet}
 return render(request, 'countries_by_letter.html', context)

def languages_list(request):
 with open("country.json", "r") as read_file:
  countries = json.loads(read_file.read())
 languages_list = set();
 for country in countries:
  for language in country['languages']:
   languages_list.add(language)
 context = {'languages':enumerate(sorted(list(languages_list)), start=1)}
 return render(request, 'languages-list.html', context)

def language(request, id):
 with open("country.json", "r") as read_file:
  countries = json.loads(read_file.read())
 languages_list = set();
 for country in countries:
  for language in country['languages']:
   languages_list.add(language)
 languages_list = sorted(list(languages_list))
 for idx, language in enumerate(languages_list, start=1):
  if idx == id:
   our_language = language
 our_countries = []
 for country in countries:
  for language in country['languages']:
   if our_language == language:
    our_countries.append(country['country'])
 context = {"countries": our_countries, "language": our_language}

 return render(request, 'language.html', context)