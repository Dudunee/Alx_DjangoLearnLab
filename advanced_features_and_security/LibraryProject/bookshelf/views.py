from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import MyModel

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request, pk):
    instance = get_object_or_404(MyModel, pk=pk)
    if request.method == 'POST':
        ...
    return render(request, 'edit_template.html', {'instance': instance})

def index(request):
    return HttpResponse("Welcome to my book store.")

# Create your views here.
