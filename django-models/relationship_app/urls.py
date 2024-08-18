from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/details/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name=), name='login'),
    path('logout/', LogoutView.as_view(template_name=), name='logout'),
    path('register/', views.register, name='register'),
]
