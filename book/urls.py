from django.urls import path
from .views import *

app_name = 'book'

urlpatterns = [
    path('', books, name='books'),
    path('book/<int:pk>/', book_details, name='book_details'),
    path('book/add/', book_create, name='book_create'),
    path('book/update/<int:pk>/', book_update, name='book_update'),
    path('book/delete/<int:pk>/', delete, name='delete'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('user/<str:username>/books/', user_books, name='user_books'),
    path('emailsent/', postdate, name='send_email'),
]
