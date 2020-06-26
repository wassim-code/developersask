from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.QuestionsListView.as_view(), name='home'),
    path('question/<int:q_id>/', views.question_detail, name='question_detail'),
    path('question/new/', views.QuestionCreateView.as_view(), name='new_question'),
]