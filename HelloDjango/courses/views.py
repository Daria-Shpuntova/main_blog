from django.shortcuts import render
from .models import Direction, Articles, Otziv, Application, Course, Lesson, Komment
from django.views.generic import ListView, CreateView, DetailView, FormView
from django.views.generic.edit import FormMixin
from .forms import ApplicationForm, CommentForm
from django.urls import reverse


# Create your views here.

class Home(ListView, FormMixin):
    model = Direction
    template_name =  'courses/video-index.html'
    context_object_name = 'directions'
    form_class = ApplicationForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.name = form.cleaned_data.get('name')
            self.phone_number = form.cleaned_data.get('phone_number')
            self.email = form.cleaned_data.get('email')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.name = self.name
        self.object.phone_number = self.phone_number
        self.object.email = self.email
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('homemarket')

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        article = Articles.objects.all()
        context['articles1'] = article.reverse()[:1]
        context['articles2'] = article.reverse()[1:5]
        context['otziv'] = Otziv.objects.all()
        return context

  #  def get_absolute_url(self):
  #      return reverse('cat_slug', args=[str(self.id)])
   #     print("/cat/" % self.Direction.slug)
   #     return "/cat/" % self.Direction.slug


class CoursesHomePage(ListView):
    model = Course
    template_name = 'courses/all_courses.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CoursesHomePage, self).get_context_data(**kwargs)
        context['title'] = 'Все курсы'
        context['directions'] = Direction.objects.all()
        return context

class Courses_slag(ListView):
    model = Course
    template_name = 'courses/course_slag.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Courses_slag, self).get_context_data(**kwargs)
        category = Direction.objects.get(slug=self.kwargs['cat_slug'])
        context['directions'] = Direction.objects.all()
        context['title'] = 'Направление: ' + category.direction
        context['courses'] = Course.objects.filter(direction = category)
        return context

class CoursePage(DetailView, FormMixin):
    model = Course
    template_name = 'courses/course_page.html'
    form_class = ApplicationForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.name = form.cleaned_data.get('name')
            self.phone_number = form.cleaned_data.get('phone_number')
            self.email = form.cleaned_data.get('email')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.name = self.name
        self.object.phone_number = self.phone_number
        self.object.email = self.email
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('homemarket')


    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CoursePage, self).get_context_data(**kwargs)
        ctx['title'] = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['lessons']=Lesson.objects.filter(course=ctx['title']).order_by('number')
        return ctx


class LessonPage(DetailView, CreateView):
    model = Course
    template_name = 'courses/les_page.html'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.text = form.cleaned_data.get('comment')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.avtor = self.request.user
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        les=list(Lesson.objects.filter(course=course).filter(slug=self.kwargs['les_slug']).values())
        ticle = les[0]['id']
        self.object.article=Lesson.objects.get(id=ticle)
        self.object.text = self.text
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LessonPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        self.les = list(Lesson.objects.filter(course=course).filter(slug=self.kwargs['les_slug']).values())
        #       print(les.query)
        ctx['title'] = self.les[0]['title']
        ctx['desk'] = self.les[0]['description']
        ctx['video'] = self.les[0]['video_url'].split('=')[1]
        ctx['comments'] = Komment.objects.filter(article=self.les[0]['id']).order_by('-date')
        return ctx

    def get_success_url(self):
        return reverse('les_page', kwargs={'slug':self.kwargs['slug'], 'les_slug': self.kwargs['les_slug']})


class ArticlesList(ListView):
    model = Articles
    template_name = 'courses/articles.html'
    context_object_name = 'articles'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticlesList, self).get_context_data(**kwargs)
        context['title'] = 'Полезные статьи'
        return context



class Art(DetailView):
    model = Articles
    template_name = 'courses/article.html'
    context_object_name = 'art_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Art, self).get_context_data(**kwargs)
        context['title'] = 'Полезные статьи'
        context['name'] = Articles.objects.filter(art_id=self.kwargs['pk'])
        context['text'] = Articles.objects.filter(art_id=self.kwargs['id'])
        context['data'] = Articles.objects.filter(art_id=self.kwargs['id'])
        return context

def arts(request, art_id):
    art = Articles.objects.filter(art_id=Articles.pk)

    return render(request, 'courses/article.html', context=art)

def art(request, art_id):
    return render(request, 'courses/article.html', {'art_id': Articles.objects.get(id=art_id), 'title': 'Полезные статьи' })