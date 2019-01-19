from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:3]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    detail_question = Question.objects.get(id=question_id)
    return render(request, 'polls/detail.html', {'detail_question' : detail_question})

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)

    try:
        data = request.POST['choice']
        print(data)
        c = q.choice_set.get(pk=data)
    except:
        return HttpResponse("there is no choice")
    c.votes = c.votes + 1
    c.save()
    return render(request, "polls/vote.html", {"q":q})
