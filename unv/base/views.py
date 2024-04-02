from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

User = get_user_model()

# Create your views here.
def homePage(request):

    if request.method == "POST":
        print("posting ....")
        username = request.POST.get("username")
        password = request.POST.get("password")
        User = authenticate(request, username = username, password = password)
        print(User)
        if User is not None:
            login(request=request, user=User)
            return redirect("student-page")
        else:
            messages.error(request, "خطأ في اسم المستخدم او كلمه السر")
    return render(request, 'home.html', context= {})

def registerPageStudent(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        civilid = request.POST.get('civilid')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            messages.error(request, "اسم المستخدم موجود بالفعل")
            return render(request, 'register-page-student.html', context= {})
        
        if User.objects.filter(email = email).exists():
            messages.error(request, "الايميل المستخدم موجود بالفعل")
            return render(request, 'register-page-student.html', context= {})
        
        
        user = User.objects.create(username = username, email = email, civilID = civilid)
        user.set_password(password)
        user.save()

        return redirect("home-page")

    return render(request, 'register-page-student.html', context= {})


def registerPageUniversity(request):
    return render(request, 'register-page-university.html', context= {})


def studentPage(request):
    return render(request, "student-page.html", context={})

