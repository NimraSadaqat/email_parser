from django.shortcuts import render
from django.utils.safestring import mark_safe

# Create your views here.
def index(request):
    with open('newspaper/email.txt', 'r', encoding="utf8") as f:
        newspaper = f.read()
    newspaper = mark_safe(newspaper)
    return render(request, 'newspaper/index.html', {'newspaper':newspaper})
