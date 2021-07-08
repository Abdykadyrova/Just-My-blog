from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from blog.wallet import wallet
from blog import views
from blog.todos_file import todos
from .models import Todo
from .models import Country
# Create your views here.
def home(request):
    title = 'главная стр'
    return render(request,'home.html',
    {
        'title':title
    })


def about(request):
    return render(request,'about.html')


def time(request):
    title = 'Страница показа времени'
    time_now = datetime.now()
    return render(request,'time.html',{
        'time_now' : time_now,
        'title':title

    })



def mywallet(request):
    return render(request,'mywallet.html', {
        'wallet': wallet
    })
def todo(request):
    # new_todo = Todo(todo_name ='Code Todo')
    # new_todo.save()
#    cur = mydb.cursor()
#    todo_list = cur.execute('''
#    SELECT * FROM todos
#    ''')
    todos_list = Todo.objects.all()
        
    

    return render(request, 'todo.html', {
        'todos': todos_list
    })



def todo_add(request):
    todo_name =request.GET.get('todo_name')
    new_todo = Todo(todo_name = todo_name)
    new_todo.save()
    return redirect('/todo')


def todo_delete(request):
    todo_id = request.GET.get('todo_id')
    todo = Todo.objects.get(id=todo_id)
    print('Mara TDOo ID:', todo_id)
    print('i find from database',todo.todo_name)
    if int(todo_id)>1:
        deleted = todo.delete()

    return redirect('/todo')



def countries(request):
    country_list = Country.objects.all()
    return render(request,'country.html',{
        'countries': country_list
    })

def country_add(request):
    new_country_name= request.GET.get('country_name')
    new_country =Country(country_name = new_country_name)
    new_country.save()
    return redirect('/countries')

   
