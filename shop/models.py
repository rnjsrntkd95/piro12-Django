from django.db import models
from django.urls import reverse
from askcompany.utils import uuid_upload_to


class Item(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<{self.pk}> {self.title}'

    # Models의 detail 파트에선 이 함수가 거의 필수임.
    # redirect() 또는 resolve_url()이 먼저 get_absolute_url()의 존재여부를 먼저 체크하고 자동으로 호출
    # 호출되면 리턴값으로 URL을 넘어가게 함
    def get_absolute_url(self):
        # return reverse('shop: item_detail', args=[self.pk])
        return reverse('shop:item_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['id']