from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice

# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list
#         }
    
#     return render(request, 'polls/index.html', context)
# -- Class-based GenericView
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self) -> QuerySet[Any]:
        return Question.objects.order_by('-pub_date')[:5]

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# logging 추가
import logging
logger =logging.getLogger(__name__)

# -- Function-based View
def vote(request, question_id):
    logger.debug('vote().question_id: %s' %question_id) # 추가
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여준다.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 정상적으로 처리하였으면,
        # 항상 HttpResponseRedirect를 반환하여 리다이렉션 처리함
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))