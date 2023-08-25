from django.http import Http404
from django.shortcuts import render, redirect

from MainApp.models import Snippet, Comment
from MainApp.forms import SnippetForm, UserRegistrationForm, CommentForm

from django.contrib.auth.decorators import login_required
from django.contrib import auth


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)

@login_required
def change_snippet_page(request, id):
    if request.method == "GET":
        if (id):
            snippet = Snippet.objects.get(id=id)
            form = SnippetForm(instance=snippet)
        else:
            form = SnippetForm()
            id = 0
        context = {
            'pagename': 'Изменение сниппета',
            'form': form,
            'id' : id
        }
        return render(request, 'pages/change_snippet.html', context)

    if request.method == "POST":
       form = SnippetForm(request.POST)
       if form.is_valid():
            if (request.user.is_authenticated):
                if (int(request.POST['id']) > 0):
                    snippet = Snippet.objects.get(id=request.POST['id'])
                    snippet.name = request.POST['name']
                    snippet.lang = request.POST['lang']
                    snippet.code = request.POST['code']
                    snippet.user = request.user
                    snippet.private = request.private
                    snippet.save()
                    return redirect("snippets_page")
                else:
                    snippet = form.save(commit=False)
                    snippet.user = request.user
                    snippet.save()
                    return redirect("snippets_page")
       context = {'pagename': 'Изменение сниппета', 'form': form }
       return render(request,'pages/change_snippet.html', context)


def snippets_page(request):
    snippets = Snippet.objects.filter(private=0) | Snippet.objects.filter(user_id=request.user.id)
    context = {'pagename': 'Просмотр сниппетов', 'snippets': snippets, 'quantity': len(snippets)}
    return render(request, 'pages/view_snippets.html', context)

def snippet(request, id):
    snippet = Snippet.objects.get(id=id)
    comments = Comment.objects.filter(snippet=id)
    form = CommentForm()
    context = {'pagename': 'Просмотр сниппета', 'id' : snippet.id, 'name': snippet.name, 'lang': snippet.lang, 'code': snippet.code, 'creation_date': snippet.creation_date, 'comments': comments, 'quantity': len(comments), 'form': form}
    return render(request, 'pages/snippet.html', context)

def snippet_create(request):
    if request.method == "POST":
       form = SnippetForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("snippets_page")
       context = {'pagename': 'Добавление нового сниппета', 'form': form }
       return render(request,'pages/change_snippet.html', context)

@login_required
def delete_snippet_page(request, id):
    snippet = Snippet.objects.get(id=id)
    snippet.delete()
    return redirect("snippets_page")

def create_user(request):
    context = {"pagename": "Регистрация пользователя"}
    if request.method == "GET":
        form = UserRegistrationForm()
        context["form"] = form
        return render(request, "pages/registration.html", context)
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context['form'] = form
        return render(request, "pages/registration.html", context)

def login(request):
    if request.method == 'POST':
       username = request.POST.get("username")
       password = request.POST.get("password")
       user = auth.authenticate(request, username=username, password=password)
       if user is not None:
           auth.login(request, user)
       else:
          context = {
              'pagename': 'home',
              'errors' : ['wrong username or password']
          }
          return render(request, 'pages/index.html', context)
    return redirect('home')

@login_required
def logout(request):
    auth.logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def my_snippets_page(request):
    snippets = Snippet.objects.filter(user_id=request.user.id)
    context = {'pagename': 'Просмотр сниппетов', 'snippets': snippets, 'quantity': len(snippets)}
    return render(request, 'pages/view_snippets.html', context)

@login_required
def comment_add(request):
   if request.method == "POST":
       comment_form = CommentForm(request.POST)
       if comment_form.is_valid():
           comment = comment_form.save(commit=False)
           comment.author = request.user
           comment.snippet = Snippet.objects.get(id=request.POST['snippet'])
           comment.save()
       return redirect('/snippet/'+str(request.POST['snippet']))

