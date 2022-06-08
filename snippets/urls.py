#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from .views import index, detail, raw

urlpatterns = [
    path('', index, name='index'),
    path('<pk>/', detail, name='detail'),
    path('<pk>/raw/', raw, name='detail-raw'),
]
