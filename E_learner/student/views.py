from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from instructor.models import Course,Cart
from instructor.forms import InstructorCreateForm
from instructor.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from student.authentication import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class StudentRegisterView(View):
    def get(self,request):
        return render(request,'student_register.html')
    
    def post(self,request):
        username=request.POST.get("username")
        name=request.POST.get("first_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            User.objects.create_user(username=username,first_name=name,email=email,password=password)
            messages.success(request,"Student Register succesfull")
            return redirect("student_login")
        except:
            messages.warning(request,"not registered")
            return redirect("student_register")



class StudentLoginView(View):
    def get(self,request):
        return render(request,"student_register.html")
    
    def post(self,request):
        username=request.POST.get("username")
        password=request.POST.get("password")
        res=authenticate(request,username=username,password=password)
        if res:
            login(request,res)
            messages.success(request,"Login Succesfull")
            if res.role == 'student':
            
                return redirect("stud_home")
            else:
                return HttpResponse("instructor")
        else:
            messages.warning(request,"invalid credentials")
            return HttpResponse("not logined")



class StudentView(View):
    def get(self,request):
        
        course = Course.objects.all()
        return render(request,"student_home.html",{"course":course})


class CourseView(View):
    def get(self,request,**kwargs):
        course=Course.objects.get(id=kwargs.get("id"))
        return render(request,'course_details.html',{"course":course})
    

@method_decorator(login_required,name="dispatch")
class AddToCartView(View):
    def get(self,request,**kwargs):
        course_instance=Course.objects.get(id=kwargs.get("id"))
        user_instance=request.user
        res_instance,created=Cart.objects.get_or_create(course_instance=course_instance,user_instance=user_instance)
        print(res_instance,created) #course_name True  
        return redirect("stud_home")
        
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("student_login")

@method_decorator(login_required,name="dispatch")
class CartSummaryView(View):
    def get(self,request):
        cart_list=Cart.objects.filter(user_instance=request.user)
        # sum=0 
        # for item in cart_list:
        #     sum+=int(item.course_instance.price)
        summ=sum([cart.course_instance.price for cart in cart_list]) # sum is decimel.decimel now
        print(type(summ))
        tax=(0.1*float(summ)) # tax is float now
        print(type(tax))
        total=tax+float(summ)
        print(total)
        return render(request,"cart_summary.html",{"cart_list":cart_list,"sum":summ,"tax":tax,"total":total})