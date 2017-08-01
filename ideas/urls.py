# -*- coding: utf-8 -*-

from django.conf.urls import url
from ideas.views import CrearIdea, TotalIdeas

urlpatterns = [
    url(r'^$', TotalIdeas.as_view(), name="ideas"),
    url(r'^crear/$', CrearIdea.as_view(), name="crear_idea")
]