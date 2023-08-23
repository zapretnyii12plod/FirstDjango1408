from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/change/<int:id>', views.change_snippet_page, name='change_snippet_page'),
    path('snippets/list', views.snippets_page, name = 'snippets_page'),
    path('snippet/<int:id>', views.snippet, name='snippet'),
    path('snippet/create', views.snippet_create, name='snippet_create'),
    path('snippets/delete/<int:id>', views.delete_snippet_page, name='delete_snippet_page'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
