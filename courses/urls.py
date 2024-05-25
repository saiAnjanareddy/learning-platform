from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, QuizViewSet, AssignmentViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'assignments', AssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
 