from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import UniversityUser

User = get_user_model()

# Create your views here.
def homePage(request):

    if request.method == "POST":
        print("posting ....")
        username = request.POST.get("username")
        password = request.POST.get("password")
        User = authenticate(request, username = username, password = password)
        if User is not None:
            login(request=request, user=User)
            if User.is_student:
                return redirect("student-page")
            if User.is_university:
                return redirect("university-page")
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
        user.is_active = True
        user.is_staff = True
        user.is_student = True
        user.set_password(password)
        user.save()

        return redirect("home-page")

    return render(request, 'register-page-student.html', context= {})


def registerPageUniversity(request):
    if request.method == "POST":
        username = request.POST["username"]
        univname = request.POST["uni-name"]
        civilid = request.POST["civilid"]
        email = request.POST["email"]
        password = request.POST["password"]

        print(username, univname, civilid, email, password )

        if User.objects.filter(username = username).exists():
            messages.error(request, "اسم المستخدم موجود بالفعل")
            return render(request, 'register-page-university.html', context= {})
        
        if User.objects.filter(email = email).exists():
            messages.error(request, "الايميل المستخدم موجود بالفعل")
            return render(request, 'register-page-university.html', context= {})
        
        
        user = UniversityUser.objects.create(username = username, email = email, civilID = civilid, universityname = univname)
        
        user.is_active = True
        user.is_staff = True
        user.is_university = True
        user.set_password(password)
        user.save()

        return redirect("home-page")

    return render(request, 'register-page-university.html', context= {})


def studentPage(request):
    
    return render(request, "student-page.html", context={})


def universityPage(request):
    
    return render(request, "university-page.html", context={})


def universityPagTap2(request):
    
    return render(request, "university-page-tap2.html", context={})



def universityPageGallery(request):
    return render(request, "university-page-gallary.html", context = {})



class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home-page")
