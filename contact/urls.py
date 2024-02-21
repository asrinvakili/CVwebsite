from django.urls import path
from contact.views import contact, news_view

app_name = 'contact'

urlpatterns = [
    path('', contact, name='contactUs'),
    path('newsletter', news_view, name='news'),

]
