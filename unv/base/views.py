from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'home.html', context= {})

def registerPageStudent(request):
    return render(request, 'register-page-student.html', context= {})


def registerPageUniversity(request):
    return render(request, 'register-page-university.html', context= {})