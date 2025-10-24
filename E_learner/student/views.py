from django.shortcuts import render,redirect
from django.views import View
from instructor.models import Course

# Create your views here.
class StudentView(View):
    def get(self,request):
        
        course = Course.objects.all()
        return render(request,"student_home.html",{"course":course})


class CourseView(View):
    def get(self,request,**kwargs):
        course=Course.objects.get(id=kwargs.get("id"))
        return render(request,'course_details.html',{"course":course})