from django.urls import path, register_converter

from . import views
from .converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, 'yyyy')

app_name = 'shop'

urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year)
]