from django.http import HttpResponse
from django.shortcuts import render


def archives_year(request, year):
    return HttpResponse(f'{year}년도에 대한 내용')
