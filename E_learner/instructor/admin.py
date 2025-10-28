from django.contrib import admin
from instructor.models import User,Category,Course,Module,Lesson,Cart

# Register your models here.
admin.site.register(User)
admin.site.register(Category)

class CourseModel(admin.ModelAdmin):
    exclude=["owner"]

admin.site.register(Course,CourseModel)

class ModuleModel(admin.ModelAdmin):
    exclude=["order"]

admin.site.register(Module,ModuleModel)

class LessonModel(admin.ModelAdmin):
    exclude=["order"]

admin.site.register(Lesson,LessonModel)
admin.site.register(Cart)