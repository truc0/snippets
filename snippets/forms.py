#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import gettext as __

from .models import LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetCreateForm(forms.Form):
    title = forms.CharField(required=False, label=__('Title'), max_length=100, help_text=__('This field is optional'))
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, help_text=__('Language'))
    code = forms.CharField(label=__('Code'), help_text=__('This is required'), widget=forms.Textarea, empty_value='')
