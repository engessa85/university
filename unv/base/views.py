from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

# Create your views here.
def homePage(request):
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


