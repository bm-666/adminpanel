from datetime import datetime as dt
from re import template

from .models import Clients
from .forms import RaitingDateForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, View
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.http import JsonResponse



class DetailClientStatics(View):
    template_name = 'client_detail.html'
    model = None
    
    @method_decorator(login_required)
    def get(self, request, db_key):
        id = Clients.objects.get(db_key=db_key).id
        resurs = self.model.objects.order_by("-date_parse").filter(table_key=id).first()
        context={
            self.model.name_model:resurs
            }
        return render(request, self.template_name,context=context) 
        

class Raiting(ListView):
    template_name = 'raiting.html'
    model = None
    
    @staticmethod
    def rating_date(args):
        print(args)
        new_date = args.split()[1:4]
        new_date = f'{new_date[1]} {new_date[0]} {new_date[2]}'
        date_rating = dt.strftime(dt.strptime(new_date, "%d %b %Y"), '%d.%m.%Y')
        return date_rating
    @method_decorator(login_required)
    def get(self, request, db_key, resurs):
        id = Clients.objects.get(db_key=db_key).id
        result = self.model.objects.order_by("-date_parse").filter(table_key=id).first()
        form = RaitingDateForm()
        context = {
            'result':result,
            'form': form
        }
        return render(request, self.template_name, context=context )
        
    @method_decorator(login_required)
    def post(self, request, db_key, resurs):
        if request.method == 'POST':
            request_date = request.POST['date_parser']
            date_parse = self.rating_date(request_date)
            id = Clients.objects.get(db_key=db_key).id
            result = self.model.objects.filter(table_key=id,date_parse=date_parse)
        
        if len(result) == 1:
            raiting = {
                'date_parse':result[0].date_parse,
                'raiting':result[0].raiting,
                'count_comments':result[0].count_comments
                }
        else:
            raiting = {
                'date_parse':0,
                'raiting':0,
                'count_comments':0
                }
        return JsonResponse(raiting)
        

