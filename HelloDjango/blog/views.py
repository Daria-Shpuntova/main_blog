from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Komment2
from .forms import CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.

#def home(request):
#    data = {
#        'news': News.objects.all(),
#        'title':'Главная страница'
#    }
#    return render(request, 'blog/home.html', data)

class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'

        return ctx

class UserNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avt=user).order_by('-date')

    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        ctx = super(UserNewsView, self).get_context_data(**kwargs)
        ctx['title'] = f"Статьи от пользователя: {self.kwargs.get('username')}"
       # ctx['some'] = 'Главная страница сайта'
        return ctx


class NewsDetaliView(DetailView, CreateView):
    model = News
    context_object_name = 'post'
    template_name = 'blog/news-detail.html'
    form_class = CommentForm
#    comment = Komment
#    print(comment.text)
#    print(model)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.text=form.cleaned_data.get('comment')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.avt = self.request.user
        self.object.article = self.get_object()
        self.object.text = self.text
        self.object.save()
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        ctx = super(NewsDetaliView, self).get_context_data(**kwargs)
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        ctx['comments'] = Komment2.objects.filter(article=self.object).order_by('-date')
        return ctx


    def get_success_url(self):
        return reverse('news-detail', kwargs={'pk': self.kwargs['pk']})



class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'blog/delete-news.html'
    success_url = '/'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avt:
            return True

        return False


class CreateNewsVies(LoginRequiredMixin ,CreateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avt = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(CreateNewsVies, self).get_context_data(**kwargs)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добаавить статью'
        return ctx

class UpdateNewsVies(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avt:
            return True

        return False

    def form_valid(self, form):
        form.instance.avt = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(UpdateNewsVies, self).get_context_data(**kwargs)

        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx


def about(request):
    return render(request, 'blog/about.html', {'title':'О нас'})

def contacts(request):
    return render(request, 'blog/cont.html', {'title':'Контакты'})

