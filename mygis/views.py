from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from mygis.models import Articles
from django.template import loader
from django.http import Http404


# Create your views here.


def home(request):
    # return HttpResponse("Hello world!")
    # return render(request, 'mygis/home.html')
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'mygis/home.html', context)


def detail(request, question_id):
    question = get_object_or_404(Articles, pk=question_id)
    return render(request, 'mygis/base.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index(request):
    latest_question_list = Articles.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'mygis/base.html', context)


def show_articles(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    return render(request, 'mygis/article.html', {'article': article})


def about(request):
    return render(request, 'mygis/about.html')