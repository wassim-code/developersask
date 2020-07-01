from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib import messages

from .models import Question, Answer
from .forms import QuestionForm

class QuestionsListView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'core/home.html'
    ordering = ['-pub_date']
    paginate_by = 10

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'You question has been added successfully!')
        return super().form_valid(form)

def question_detail(request, q_id):
    question = get_object_or_404(Question, id=q_id)
    if request.method == "POST" and request.user.is_authenticated:
        answer = Answer.objects.create(
            question=question,
            author=request.user,
            body=request.POST['answer_body'],
            )
        answer_dict = {'author': answer.author.username, 'pub_date': answer.pub_date, 'body': answer.body}
        context = {'alert_msg': 'Your answer has been added successfully!', 'answer': answer_dict}
        return JsonResponse(context, safe=False)
    return render(request, 'core/question_detail.html', {'question': question})

def handler404(request, *args, **kwargs):
    return render(request, '404.html', status=404)

def handler500(request, *args, **kwargs):
    return render(request, '500.html', status=500)