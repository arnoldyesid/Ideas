# -*- coding: utf-8 -*-
from django import forms
from ideas.models import Ideas


class FormIdea(forms.ModelForm):
    class Meta:
        model = Ideas
        exclude = ["owner","user_likes","status","slug","publish"]

