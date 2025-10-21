from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from instructor.models import User
from instructor.forms import InstructorCreateForm
from django.contrib.auth.hashers import make_password


# Create your views here.

class InstructorCreateView(View):
    def get(self,request):
        form=InstructorCreateForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request):
        form_instance=InstructorCreateForm(request.POST)
        if form_instance.is_valid():
            res=form_instance.save(commit=False)
            res.is_superuser=True
            res.is_staff=True
            res.role="instructor"
            res.password=make_password(form_instance.cleaned_data.get("password"))
            res.save()
            return HttpResponse("added")