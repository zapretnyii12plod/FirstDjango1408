from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='add_snippet_page'),
    path('snippets/list', views.snippets_page, name = 'snippets_page'),
    path('snippet/<int:id>', views.snippet, name='snippet'),
    path('snippet/create', views.snippet_create, name='snippet_create'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
