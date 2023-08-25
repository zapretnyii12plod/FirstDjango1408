from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='home'),
    path('snippets/change/<int:id>', views.change_snippet_page, name='change_snippet_page'),
    path('snippets/list/order/<str:order_name>', views.snippets_page, name = 'snippets_page'),
    path('snippet/<int:id>', views.snippet, name='snippet'),
    path('snippet/create', views.snippet_create, name='snippet_create'),
    path('snippets/delete/<int:id>', views.delete_snippet_page, name='delete_snippet_page'),
    path('auth/register', views.create_user, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('snippets/list/my/order/<str:order_name>', views.my_snippets_page, name = 'my_snippets'),
    path('comment/add', views.comment_add, name='comment_add')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
