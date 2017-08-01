# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView
from ideas.forms import FormIdea
from ideas.models import Ideas


class CrearIdea(View):
    def get(self,request):
        form = FormIdea()
        context ={
            'form':form,
        }
        return render(request, 'ideas/crear_idea.html', context)

    def post(self,request):
        form = FormIdea(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()

        return render(request, "ideas/crear_idea.html")


class Ideas_user(ListView):
    models = Ideas
    template_name = 'ideas/user_ideas.html'

    def get_queryset(self):
        queryset = super(Ideas_user,self).get_queryset()
        return queryset.filter(owner=self.request.user)


class TotalIdeas(ListView):
    queryset = Ideas.objects.all()
    context_object_name = 'ideas'
    template_name = "ideas/ideas.html"
    paginate_by = 9
