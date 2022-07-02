from django.shortcuts import render, get_object_or_404

from izo.models import *


def index(request):
    context = {
        'title': 'izo studio',
        'services': Category.objects.all(),
        # 'souvenirs': Services.objects.filter(cat_id=2),
        # 'services_title':'фотоуслуги',
        # 'souvenirs_title':'фотосувениры',
        # 'posts': Post.objects.get(id=1),
    }
    return render(request, 'izo/index.html', context=context)
