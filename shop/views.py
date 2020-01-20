import logging
import re
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Item
from .forms import ItemForm
from django.views.generic import CreateView, UpdateView


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

# FBV 함수 기반 뷰
# def item_new(request, item=None):
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES, instance=item)
#         if form.is_valid():
#             item = form.save()  # ModelForm에서 제공
#             return redirect(item)
#     else:
#         form = ItemForm(instance=item)
#     return render(request, 'shop/item_form.html', {
#         'form': form,
#     })


# def item_edit(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     return item_new(request, item)


# CBV 클라스 기반 뷰
item_new = CreateView.as_view(model=Item, form_class=ItemForm)
item_edit = UpdateView.as_view(model=Item, form_class=ItemForm)

