from datetime import datetime as dt


from re import template
from django.shortcuts import render 
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Clients, Comments, Yandex
from .utils import Raiting, DetailClientStatics


class Statistics(View):
    template_name = 'statistics.html'
    clients = Clients.objects.all()
    
    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name, context={"clients":self.clients})

class YandexClientStatics(DetailClientStatics):
    model = Yandex

class ResursComments(View):
    template_name = 'resurs_commets.html'
    
    @method_decorator(login_required)
    def get(self, request, db_key, resurs):
        id = Clients.objects.get(db_key=db_key).id
        comments = [i for i in Comments.objects.filter(comment_resurs=resurs, comment_key=id)]
        comments.sort(key=lambda i: dt.strptime(i.date_comment, "%d.%m.%Y").date(), reverse=True)
        return render(request, self.template_name, context={'comments': comments})

class YandexRaiting(Raiting):
    model = Yandex
