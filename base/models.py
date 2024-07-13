from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_description = models.TextField(null=True, blank=True)
    learning_outcome = models.TextField(null=True, blank=True)
    software_required = models.CharField(max_length=255, null=True, blank=True) 
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    syllabus = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['start_date']

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("End date should be after start date.")



    def __str__(self):
        return f"{self.course_name} - {self.instructor}"
    


class Enrollment(models.Model):

    enrollment_status_choices = [
        ("active","Active"),
        ("completed", "Completed"),
        ("dropped","Dropped")

    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments", default=1)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=enrollment_status_choices, default='active')
    grade = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.course_name}"



class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="assignments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"
        ordering = ['due_date']

    def __str__(self):
        return f"{self.title} from {self.course}"

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions")
    submission_date = models.DateTimeField(auto_now=True)
    content = models.FileField(null=True, blank=True)
    grade = models.IntegerField(null=True, blank=True)
    feedback = models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"
        ordering = ['submission_date']

    def __str__(self):
        return f"{self.assignment} submitted by {self.student}"
    


    




# class Lesson(models.Model):
#     pass 



# class Attendance(models.Model):
#     pass 