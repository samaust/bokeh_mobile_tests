from django.urls import path

from . import views

app_name = "bokeh_mobile_tests"

urlpatterns = [
    path('plot001/', views.plot001, name='plot001'),
]