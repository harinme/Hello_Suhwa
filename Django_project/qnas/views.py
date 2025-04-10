from django.shortcuts import render, redirect
from .models import Qna
from .forms import QnaForm

# Create your views here.
def index(request):
    qnas = Qna.objects.all()
    context = {
        'qnas':qnas,
    }

    return render(request, 'qnas/index.html', context)

def detail(request, qna_pk):
    qna = Qna.objects.get(pk=qna_pk)

    context = {
        'qna':qna,
    }
    return render(request, 'qnas/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = QnaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('qnas:index')
    else:
        form = QnaForm()
    context= {
        'form':form,
    }
    return render(request, 'qnas/create.html', context)

def delete(request, qna_pk):
    qna = Qna.objects.get(pk= qna_pk)
    qna.delete()
    return redirect('qnas:index')