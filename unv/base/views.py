from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import UniversityUser, UniversityData
from .alluniv import UNIVERSITIES

User = get_user_model()

# Create your views here.
def homePage(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        User = authenticate(request, username = username, password = password)
        if User is not None:
            login(request=request, user=User)
            if User.is_student:
                return redirect("student-page")
            if User.is_university:
                if UniversityData.objects.filter(user = User).exists():
                    print("existed")
                    return redirect("university-page-gallery")
                else:
                    return redirect("university-main-page")
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







def universityMainPage(request):
    
    if request.method == 'POST':

        
        student_email = request.POST.get('studentemail')
        aboutunv = request.POST.get('aboutunv')
        score1 = request.POST.get('score1')
        score2 = request.POST.get('score2')
        score3 = request.POST.get('score3')
        score4 = request.POST.get('score4')
        score5 = request.POST.get('score5')
        score6 = request.POST.get('score6')

        
        request.session['student_email'] = student_email
        request.session['about_unv'] = aboutunv
        request.session['score1'] = score1
        request.session['score2'] = score2
        request.session['score3'] = score3
        request.session['score4'] = score4
        request.session['score5'] = score5
        request.session['score6'] = score6


        return redirect("university-more-info")


    else:
        print("here")

    return render(request, "university-main-page.html", context={})


def universityMoreInfo(request):

    if request.method == 'POST':
        print("Inside POST block")

        unvUser = request.user

        student_email = request.session.get('student_email')
        about_unv = request.session.get('about_unv')
        score1 = request.session.get('score1')
        score2 = request.session.get('score2')
        score3 = request.session.get('score3')
        score4 = request.session.get('score4')
        score5 = request.session.get('score5')
        score6 = request.session.get('score6')
        
        specialization1 = request.POST.get('specialization1')
        seats1 = request.POST.get('seats1')
        college1 = request.POST.get('college1')
        acceptance_rate1 = request.POST.get('acceptance_rate1')


        # Print all the values
        # print("User:", unvUser)
        # print("Student Email:", student_email)
        # print("About University:", about_unv)
        # print("Score 1:", score1)
        # print("Score 2:", score2)
        # print("Score 3:", score3)
        # print("Score 4:", score4)
        # print("Score 5:", score5)
        # print("Score 6:", score6)
        # print("Specialization 1:", specialization1)
        # print("Seats 1:", seats1)
        # print("College 1:", college1)
        # print("Acceptance Rate 1:", acceptance_rate1)
        
        try:
            UniversityData.objects.create(
            user=unvUser,
            student_email=student_email,
            about_university=about_unv,
            score1=score1,
            score2=score2,
            score3=score3,
            score4=score4,
            score5=score5,
            score6=score6,
            specialization1=specialization1,
            seats1=seats1,
            college1=college1,
            acceptance_rate1=acceptance_rate1
        )
        except Exception as e:
          
            print(e)

        return redirect("university-page-gallery")
    
    return render(request, "university-more-info.html", context={})
    






def universityPage(request):
    
    return render(request, "university-page.html", context={})


def universityPagTap2(request):
    
    return render(request, "university-page-tap2.html", context={})



def universityPageGallery(request):
    return render(request, "university-page-gallary.html", context = {})







def universityGetInfoPage(request, image_filename):
    path = f"images/uni/{image_filename}"
    print(image_filename)

    university_info = UNIVERSITIES.get(image_filename)
    university_name = university_info.get('name')
    description = university_info.get('description')

    print(university_info, university_name, description)

    context = {
        "path":path,
        "university_name":university_name,
        "description":description


    }

    return render(request, "university-get-info.html", context = context)








class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home-page")
