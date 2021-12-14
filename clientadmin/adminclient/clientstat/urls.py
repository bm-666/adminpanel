"""adminclient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from clientstat.views import Statistics, DetailClientStatics, ResursComments, YandexRaiting


urlpatterns = [
    path('', Statistics.as_view(), name='statistics'),
    path('<str:db_key>', DetailClientStatics.as_view(), name='detail'),
    path('<str:db_key>/<str:resurs>', ResursComments.as_view(), name='comments'),
    path('<str:db_key>/<str:resurs>/raiting', YandexRaiting.as_view(), name='yandex'),
    path('<str:db_key>/<str:resurs>/date_parse', YandexRaiting.as_view(), name='date_parse')

]
