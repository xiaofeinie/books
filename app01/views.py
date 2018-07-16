from django.shortcuts import render,redirect

# Create your views here.
from app01.models import Book


def index(request):
    ret = Book.objects.all()
    return render(request,'index.html',{'ret':ret})


def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish = request.POST.get('publish')

        Book.objects.create(title=title,price=price,pub_date=pub_date,publish=publish)

        return redirect('/index/')

    return render(request, 'add_book.html')


def updbook(request):
    id = request.GET.get('id')
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish = request.POST.get('publish')
        Book.objects.filter(id=id).update(title=title,price=price,pub_date=pub_date,publish=publish)

        return redirect('/index/')

    ret = Book.objects.get(id=id)
    return render(request, 'updbook.html', {'title':ret.title, 'price':ret.price,'pub_date':ret.pub_date,'publish':ret.publish})


def delbook(request):
    id = request.GET.get('id')
    Book.objects.filter(id=id).delete()
    return redirect('/index/')
