
Book.objects.filter(author__name='Author Name')

Library.objects.get(name='Library Name').books.all()

"Librarian.objects.get(name=Library Name)"
