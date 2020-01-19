import logging
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from shop.models import Item

logger = logging.getLogger(__name__)

def archives_year(request, year):
    return HttpResponse(f'{year}년도에 대한 내용')


def item_list(request):
    qs = Item.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    logger.debug(f'query : {q}')

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q,
    })

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item
    })