from django.contrib import admin
from .models import Course, Lecture, Quiz, Assignment

class LectureInline(admin.TabularInline):
    model = Lecture
    extra = 1

class QuizInline(admin.TabularInline):
    model = Quiz
    extra = 1

class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'level', 'created_at', 'updated_at')
    search_fields = ('title', 'category', 'level')
    list_filter = ('category', 'level')
    inlines = [LectureInline, QuizInline, AssignmentInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture)
admin.site.register(Quiz)
admin.site.register(Assignment)
