# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def get_index_page(request):

	return HttpResponse('get index pdage my test')
