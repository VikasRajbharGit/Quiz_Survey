from django.contrib import admin
from .models import Quiz, QuizResponse, QuestionResponse, Question, Answer

# Register your models here.
admin.site.register(Quiz)
admin.site.register(QuizResponse)
admin.site.register(QuestionResponse)
admin.site.register(Question)
admin.site.register(Answer)
#admin.site.register()
#admin.site.register()
