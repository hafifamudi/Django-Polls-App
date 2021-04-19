from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list
    }

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=1)
    except Question.DoesNotExist:
        raise Http404("Question Doesn't exist")
    
    return render(request, 'polls/detail.html', {'question':question})


def results(request, question_id):
    response = "You're looking at question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)