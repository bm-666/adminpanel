from re import template
from django.shortcuts import render 
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Clients, Comments, Yandex
from .utils import Raiting


class Statistics(View):
    template_name = 'statistics.html'
    clients = Clients.objects.all()
    
    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name, context={"clients":self.clients})

class DetailClientStatics(View):
    template_name = 'client_detail.html'
    
    @method_decorator(login_required)
    def get(self, request, db_key):
        id = Clients.objects.get(db_key=db_key).id
        yandex = Yandex.objects.order_by("-date_parse").filter(yandex_key=id).first()
        print(yandex.date_parse)

        return render(request, self.template_name, context={'yandex':yandex})

class ResursComments(View):
    template_name = 'resurs_commets.html'
    
    @method_decorator(login_required)
    def get(self, request, db_key, resurs):
        id = Clients.objects.get(db_key=db_key).id
        comments = Comments.objects.filter(comment_resurs=resurs, comments_key=id)
        return render(request, self.template_name, context={'comments': comments})

class YandexRaiting(Raiting):
    model = Yandex
