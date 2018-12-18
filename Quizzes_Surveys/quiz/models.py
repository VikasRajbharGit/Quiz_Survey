from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('users.Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.quiz.title.upper() + ' Question'}"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    correct = models.BooleanField(blank=False, default=False, help_text="Is this a correct answer?")

    def __str__(self):
        return f"{self.content}"


class QuestionResponse(models.Model):
    student = models.OneToOneField('users.Student', on_delete=models.CASCADE)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Response to {self.question.quiz.title.upper()} + Question - {self.question.text}"


class QuizResponse(models.Model):
    student = models.OneToOneField('users.Student', on_delete=models.CASCADE)
    quiz = models.OneToOneField(Quiz, on_delete=models.CASCADE)
    responses = models.ForeignKey(QuestionResponse, on_delete=models.CASCADE)
    score = 0

    def __str__(self):
        return f"{self.quiz.title.upper() + ' Question'}"

    def get_result(self):
        if self.responses.question.answer_set[0] == self.responses.answer:
            self.score += 1
        return self.score
