from django.urls import path
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/details/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name=), name='login'),
    path('logout/', LogoutView.as_view(template_name=), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]
