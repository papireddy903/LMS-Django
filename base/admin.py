from django.contrib import admin
from .models import Course, Enrollment, Assignment, Submission

# Register your models here.


admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Assignment)
admin.site.register(Submission)