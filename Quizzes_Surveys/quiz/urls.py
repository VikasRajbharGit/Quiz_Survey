from django.urls import path
from . import views
from .views import QuizListView


urlpatterns = [
    path('', QuizListView.as_view(), name='quiz-list'),
    path('quiz/<int:pk>/', views.question_list, name='quiz-detail')
]
