from django.shortcuts import render , redirect
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import authenticate,login
from profiles.models import Profile ,Record
from books.models import Book
from django.utils.timezone import now

def issue(request):
    code = request.GET.get('code')
    book = Book.objects.filter(accessNo=code)
    if book[0].availible==True:
        if request.method == "POST":
            username       = request.POST["id"]
            password    = request.POST["pass"]

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                record  =  Record(acc = code,issue=now(),user=user )
                record.save()
                book.update(availible=False)
                return redirect('login')

            else:
                return render(request,"401.html")
    
    elif request.method == "POST":
        username       = request.POST["id"]
        password    = request.POST["pass"]

        if username == "librarian" and password == '25654':
            record = Record.objects.filter(acc=code).filter(back=None)
            record.update(back=now())
            Book.objects.filter(accessNo=code).update(availible=True)


        


    return render(request,"issue.html")





def home(request):

    books   = Book.objects.all()

    return render(request,'index.html',{'books':books})



def Signin(request):

    if request.method=="POST":

        username       = request.POST["id"]
        password    = request.POST["pass"]

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            

            return redirect('dashboard')

        else:
            return render(request,"401.html")
    return render(request,'login.html')


def dashboard(request):

    user  = request.user

    record  = Record.objects.filter(user=user)
    profile = Profile.objects.filter(user=user)


    context = {
        'record':record,
        'profile':profile,

    }
    return render(request,'dashboard.html',context)