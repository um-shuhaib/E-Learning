from django.contrib import admin
from instructor.models import User,Category,Course,Module

# Register your models here.
admin.site.register(User)
admin.site.register(Category)

class CourseModel(admin.ModelAdmin):
    exclude=["owner"]

admin.site.register(Course,CourseModel)
admin.site.register(Module)