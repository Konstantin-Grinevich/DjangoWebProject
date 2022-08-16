from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, Publisher
from .form import PostForm

def booksDetail(request, id=None):
    instance=Book.objects.get(id=id)
    status = ''
    if instance.status == 'r1':
        status = 'Роман'
    elif instance.status == 'p':
        status = 'Поэма'
    elif instance.status == 's':
        status = 'Стихотворение'
    elif instance.status == 'r2':
        status = 'Рассказ'
    context={
            'instance':instance,
            'status':status,
        }
    return render(request, 'Books/bookDetail.html',context)

def authorDetail(request, id=None):
    instance = Author.objects.get(id=id)
    context={
            'instance':instance,
        }
    return render(request, 'Books/authorDetail.html', context)

def booksList(request):
    queryset=Book.objects.all()
    context={
            'queryset':queryset,
            'title':'Список книг',
        }
    return render(request, 'Books/index.html',context)

def bookCreate(request):
    form=PostForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
    context={
            'form':form
        }
    return render(request,'Books/createBook.html',context)

def bookUpdate(request, id):
    instance=Book.objects.get(id=id)
    form=PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
    context={
            'title':instance.title,
            'instance':instance,
            'form':form,
        }
    return render(request,'Books/createBook.html',context)

def pubDetail(request, id=None):
    instance = Publisher.objects.get(id=id)
    context={
            'instance':instance,
        }
    return render(request, 'Books/pubDetail.html', context)