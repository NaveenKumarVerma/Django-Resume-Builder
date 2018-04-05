from django.shortcuts import render

def index(request):
    return render(request, 'mysite/home.html')

def about(request):
    return render(request,'mysite/about.html',{'ctent':['Resume Builder is a simple website that helps you to build your resume in easy manner.',                                                           'User can download the resume built in this website in pdf format.']})

def contact(request):
    return render(request, 'mysite/contact.html',{'ctent':['Developer- Naveen Kumar Verma','Email- n16verma@gmail.com']})
