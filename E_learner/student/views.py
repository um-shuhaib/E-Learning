from django.shortcuts import render,redirect
from django.views import View

# Create your views here.
class StudentView(View):
    def get(self,request):
        return render(request,"student_home.html")