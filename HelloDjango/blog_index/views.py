from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Progects, Tags
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .forms import ContactForm
from HelloDjango.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# Create your views here.

class HomePage(ListView, FormMixin):
    model = Progects
    template_name = 'blog_index/index.html'
    context_object_name = 'progects'
    form_class = ContactForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email}', message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return HttpResponseRedirect(reverse('home') )
        else:
            return HttpResponse('Неверный запрос.')
        return render(request,"blog_index/index.html", {'form': form})


    def get_success_url(self):
        return reverse('home')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница блога'
        context['tags'] = Tags.objects.filter(tag=self.model.tags)
        context['all_tags'] = Tags.objects.all
        context['prog'] = Progects.objects.all().order_by('-data')[:2]
        return context


class Works(ListView):
    model = Progects
    template_name = 'blog_index/works.html'
    context_object_name = 'progects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Works, self).get_context_data(**kwargs)
        context['title'] = 'Мои работы'
        context['tags'] = Tags.objects.filter(tag=self.model.tags)
        context['all_tags'] = Tags.objects.all
        return context


class Progect_page(DetailView):
    model = Progects
    template_name = 'blog_index/prog_id.html'
    context_object_name = 'progect'
    pk_url_kwarg = 'prog_id'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Progect_page, self).get_context_data(**kwargs)
        context['title'] = Progects.objects.filter(pk=self.kwargs['prog_id']).first()
        context['prog'] = Progects.objects.filter(pk=self.kwargs['prog_id'])
        context['tags'] = Tags.objects.filter(tag=self.model.tags)
        context['all_tags'] = Tags.objects.all
        return context

def about_me(request):
    return render(request, 'blog_index/about_me.html')

class Tag_id(DetailView):
    model = Progects
    template_name = 'blog_index/tag.html'
    context_object_name = 'tagss'
    pk_url_kwarg = 'tag_id'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Tag_id, self).get_context_data(**kwargs)
        nameProgect =  Progects.objects.filter(tags=self.kwargs['tag_id'])
        context['name_progect'] = Progects.objects.filter(tags=self.kwargs['tag_id'])
        context['title'] = Tags.objects.filter(pk=self.kwargs['tag_id']).first()
        context['tags'] = Tags.objects.filter(tag=self.model.tags)
        context['all_tags'] = Tags.objects.all
        return context
