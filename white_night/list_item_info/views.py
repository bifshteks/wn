# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from list_item_info.models import ItemInfo
from django.views.generic import ListView, DetailView

class PostsListView(ListView): # представление в виде списка
    model = ItemInfo                   # модель для представления 

class PostDetailView(DetailView): # детализированное представление модели
    #model = ItemInfo

	def iteminfo_detail(request, pk):
		item = get_object_or_404(ItemInfo, pk=pk)
		return render(request, 'list_item_info/iteminfo_detail.html', {'item': item})





