from django.shortcuts import render
from .models import Qna

# Create your views here.
def index(request):
    qnas = Qna.objects.all()
    context = {
        'qnas':qnas,
    }

    return render(request, 'qnas/index.html', context)