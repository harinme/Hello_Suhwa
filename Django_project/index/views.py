from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'intro/index.html')

def words(request):
    return render(request, 'intro/words.html')