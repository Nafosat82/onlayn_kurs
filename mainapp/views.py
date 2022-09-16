from django.shortcuts import render
from mainapp.models import HeaderCarousel, Student
from .forms import RegisterModelForm


def index(request):
    ads = HeaderCarousel.objects.all()
    if request.method == "POST":
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            form.save()
            # name = form.data.get("name")
            # email = form.data.get("email")
            # course = form.data.get("course")
            # Student.objects.create(name=name, email=email, course=course)
    

  
    for ad in ads:
        ad_title = ad.title[:5]
    form = RegisterModelForm()      
    context = {
        "form":form,
        "ads":ads,
             }
    return render(request, 'index.html', context=context)



def about(request):
    return render(request,'about.html')


def course(request):
    return render(request,'course.html')


def teacher(request):
    return render(request,'teacher.html')


def blog(request):
    return render(request,'blog.html')

def blog_detail(request):
    return render(request,'single.html')

def contact(request):
    return render(request,'contact.html')