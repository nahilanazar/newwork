from django.contrib import admin
from.models import *
# Register your models here.

class department_display(admin.ModelAdmin):
    list_display=['dep_name']

class batch_display(admin.ModelAdmin):
    list_display=['batch_time']

class student_display(admin.ModelAdmin):
    list_display=['std_name','address','dept']




admin.site.register(Department,department_display)  
admin.site.register(Batch,batch_display)
admin.site.register(student,student_display) 


