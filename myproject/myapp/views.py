from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):
    # return HttpResponse('<h1> hi welcome </h1>')  # An html file here only

    #return render(request, 'index.html')  # rendering/importing an html file 

    '''
    name='Ayush'
    name=user.name  (any name coming from a database which is being created)
    return render(request, 'index.html', {'name':name}) '''   # {key : value}

    context={
        'name':'Ayush',
        'age':26,
        'nationality':'indian'
    }
    # return render(request, 'index.html', context)

    # creating objects of Student class
    s1=Student()
    s1.id=1
    s1.name='abc'

    s2=Student()
    s2.id=2
    s2.name='ghj'

    s3=Student()
    s3.id=3
    s3.name='xyz'

    students=[s1,s2,s3]
    # return render(request, 'index.html', {'students':students})



    # importing objects directly from DB
    features = Feature.objects.all()      # a list containing of all the objects of Feature class

    return render(request, 'index.html', {'features':features})



def counter(request):
    # words=request.GET['words']
    words=request.POST['words']
    no_of_words=len(words.split())
    return render(request,'counter.html', {'amount':no_of_words})



def register(request):

    if request.method=='POST':
        username = request. POST['username']
        email = request. POST['email']
        password = request. POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    
    else:
        return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        username = request. POST['username']
        password = request. POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')       # redirecting to home page
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect ('login')
    else:
        return render (request, 'login.html')
    


def logout(request):
    auth.logout(request)
    return redirect('/')



# Dynamic URL routing 

def post(request, pk):
    posts=[1,2,3,4]
    # return render(request, 'post.html', {'posts': posts})
    return render(request, 'post.html', {'pk': pk})