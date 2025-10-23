from django.shortcuts import render,redirect
from django.views import View
from instructor.models import Course

# Create your views here.
class StudentView(View):
    def get(self,request):
        
        course = Course.objects.all()
        return render(request,"student_home.html",{"course":course})