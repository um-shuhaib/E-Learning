"""
URL configuration for E_learner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from instructor import views
from student import views as studView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("instructor/register",views.InstructorCreateView.as_view(),name="register"),
    path("student/home",studView.StudentView.as_view(),name="stud_home"),
    path("student/details/<int:id>",studView.CourseView.as_view(),name="course_detail"),
    path("student/register",studView.StudentRegisterView.as_view(),name="student_register"),
    path("student/login",studView.StudentLoginView.as_view(),name="student_login"),
    path("student/addtocart/<int:id>",studView.AddToCartView.as_view(),name="add_to_cart"),
    path("student/logout",studView.LogoutView.as_view(),name="logout"),
    path("cart/summary",studView.CartSummaryView.as_view(),name="cart_summary"),
    path("cart/delete/<int:id>",studView.DeleteCartView.as_view(),name="cart_delete"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
