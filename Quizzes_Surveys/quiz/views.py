from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, QuizResponse, QuestionResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import AccessMixin


# Create your views Question

class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/home.html'
    context_object_name = 'quizzes'


def question_list(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    context = {
        'questions': Question.objects.filter(quiz=quiz)

    }
    return render(request, 'quiz/show_quiz.html', context)

